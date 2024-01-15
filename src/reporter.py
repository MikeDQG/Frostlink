from collections import namedtuple
import retriever
import db_object
import writer
import listener

class Reporter():

    def __init__(self):
        self.retriever = retriever.Retriever()
        self.Values_tuple = namedtuple('Values', ['message', 'capacity', 'temp1', 'temp2', 'temp3', 'temp4', 'active_alarm_count', 'alarm_name'])
        self.writer = writer.Writer()
        self.listener = listener.Listener()
    
    def main(self):
        self.update()
        self.write()
        self.listen()
    
    def update(self):
        # get active alarms count and report it
        # retrieve data and write it
        self.db_object = self.retriever.get_values()

    def write(self):
        self.writer.write(self.Values_tuple)
    
    def listen(self):
        self.listener.listen()
        if self.listener.confirm_alarms != None:
            print("Incomplete code: Reporter: 31")
            """ torej tukaj moramo resetirat alarme """
            self.retriever.confirm_alarms()