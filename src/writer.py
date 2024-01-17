from collections import namedtuple

class Writer():
    def __init__(self):
        self.namedtuple_output = namedtuple('Values', ['message', 'capacity', 'temp1', 'temp2', 'temp3', 'temp4', 'active_alarm_count', 'alarm_name'])
        print("Writer init")

    def write(self, namedtuple_input):
       #self.namedtuple_output = namedtuple_input
       #print("Writer write ", self.namedtuple_output)
       print("Writer write ", namedtuple_input)
       """ following: send to DB, each value """
