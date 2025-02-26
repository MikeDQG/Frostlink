from collections import namedtuple
import requester
import logging
import json

# if testing doesn't work, try this in terminal: $env:PYTHONPATH="src/"

class Retriever():
    def __init__(self):
        self.req = requester.Requester()
        self.alarms = None
        self.values = None
        self.monitoring_updates = None
        self.Values_tuple = namedtuple('Values', ['message', 'capacity', 'temp1', 'temp2', 'temp3', 'temp4', 'active_alarm_count', 'alarm_name'])
        logging.debug("Retriever initialized")
        
    def get_values(self):
        '''getPointValue'''
        #print('values get')
        self.values = self.req.get_point_value()

        self.monitoring_updates = self.req.monitoring()
        #print("Retriever: line 22: monitoring_updates", self.monitoring_updates)
        #print("Retriever: line 23: active_alarm_count", self.monitoring_updates['active_alarm_count'])

        if int(self.monitoring_updates['active_alarm_count']) > 0:
            #print('active_alarm_count > 0')
            self.alarms = self.get_alarms()
            #print(self.alarms)
        #print('29: values saved 2')
        self._update_values()
        self._save_db_values()

        return self.final_values

    def confirm_alarms(self):
        '''confirm alarms'''
        self.req = requester.Requester()
        try:
            self.req.confirm_alarms()
        except KeyboardInterrupt as KI:
            logging.exception(KI)
            raise KeyboardInterrupt
        except Exception as e:
            logging.exception(e)
    
    def get_alarms(self):
        return self.req.get_alarms()
        
    def logout(self):
        self.req.logout()
        self.req = requester.Requester()

    def end_session(self):
        self.req.logout()
        #print("Session ended")

    def _update_values(self):
        #print('values getting updated')
        temporary_values = []
        for value in self.values['pathlist']:
            value = { "path": value['path'], "value": value['value'] }
            temporary_values.append(value)
        self.values = temporary_values
        #print('values updated')

    def _save_db_values(self):
        def f_to_c(f):      # Fahrenheit to Celsius
            c = f - 32.0
            return c * 5 / 9
        def msg_to_slo(msg):
            dictionary = {
                "Local  Off": "Izklopljeno",
                "Local   Off": "Izklopljeno",
                "Local    Off": "Izklopljeno",
                "Stopping": "Zaustavljanje",
                "Local On": "Vklopljeno",
                "Local  On": "Vklopljeno",
                "Local   On": "Vklopljeno",
                "Local    On": "Vklopljeno",
                "Local    Running": "Vklopljeno",
                "Remote   Off": "Izklopljeno",
                "Remote   Running": "Daljinski vklop"
            }
            
            try:
                #with open('../pasice.json', 'r') as file:
                #with open('../app/pasice.json', 'r') as file:
                with open('../../pasice.json', 'r') as file:
                    data = json.load(file)
                return data[msg]
            except KeyboardInterrupt as KI:
                logging.exception(KI)
                raise KeyboardInterrupt
            except Exception as some_exception:
                logging.warning(some_exception)
            try:
                return dictionary[msg]
            except Exception as another_exception:
                logging.warning(another_exception)
                return msg
        #print('values getting saved')
        temporary_val_list = []
        temporary_val_list.append(msg_to_slo(self.values[0]['value']))
        temporary_val_list.append(int(self.values[1]['value']))
        temporary_val_list.append(f_to_c(float(self.values[2]['value'])))
        temporary_val_list.append(f_to_c(float(self.values[3]['value'])))
        temporary_val_list.append(f_to_c(float(self.values[4]['value'])))
        temporary_val_list.append(f_to_c(float(self.values[5]['value'])))
        temporary_val_list.append(int(self.monitoring_updates['active_alarm_count']))
        temporary_val_list.append(None)
        self.final_values = self.Values_tuple._make(temporary_val_list)
        #print(self.final_values._asdict())