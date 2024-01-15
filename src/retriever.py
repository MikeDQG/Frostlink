from collections import namedtuple
import requester
import db_object

# if testing doesn't work, try this in terminal: $env:PYTHONPATH="src/"

class Retriever():
    def __init__(self):
        self.req = requester.Requester()
        self.alarms = None
        self.values = None
        self.monitoring_updates = None
        self.Values_tuple = namedtuple('Values', ['message', 'capacity', 'temp1', 'temp2', 'temp3', 'temp4', 'active_alarm_count', 'alarm_name'])

    def get_values(self):
        '''getPointValue'''
        self.values = self.req.get_point_value()

        self.monitoring_updates = self.req.monitoring()
        #print("Retriever: line 22: monitoring_updates", self.monitoring_updates)
        #print("Retriever: line 23: active_alarm_count", self.monitoring_updates['active_alarm_count'])

        if int(self.monitoring_updates['active_alarm_count']) > 0:
            self.alarms = self.get_alarms()
            #print(self.alarms)
        """ update db_send_object """
        self._update_values()
        self._save_db_values()

        return self.Values_tuple

    def confirm_alarms(self):
        '''confirm alarms'''
        self.req = requester.Requester()
        try:
            self.req.confirm_alarms()
        except:
            print("except")
    
    def get_alarms(self):
        return self.req.get_alarms()
        
    def logout(self):
        self.req.logout()
        self.req = requester.Requester()

    def end_session(self):
        self.req.logout()
        print("Session ended")

    def _update_values(self):
        temporary_values = []
        for value in self.values:
            value = { "path": value['path'], "value": value['value'] }
            temporary_values.append(value)
        self.values = temporary_values

    def _save_db_values(self):
        def f_to_c(f):      # Fahrenheit to Celsius
            c = f - 32.0
            return c * 5 / 9
        self.Values_tuple.message = self.values[0]['value']
        self.Values_tuple.capacity = int(self.values[1]['value'])
        self.Values_tuple.temp1 = f_to_c(float(self.values[2]['value']))
        self.Values_tuple.temp2 = f_to_c(float(self.values[3]['value']))
        self.Values_tuple.temp3 = f_to_c(float(self.values[4]['value']))
        self.Values_tuple.temp4 = f_to_c(float(self.values[5]['value']))
        self.Values_tuple.active_alarm_count = int(self.monitoring_updates['active_alarm_count'])
        self.Values_tuple.alarm_name = None