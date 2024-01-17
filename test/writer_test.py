import writer
import mysql.connector
from collections import namedtuple

send_tuple_dict = {'message': 'Local    Running', 'capacity': 75, 'temp1': 22.84566222222222, 'temp2': 5.449184999999998, 'temp3': 3.379012222222223, 'temp4': 26.772223333333336, 'active_alarm_count': 0, 'alarm_name': None}
Values_tuple = namedtuple('Values', ['message', 'capacity', 'temp1', 'temp2', 'temp3', 'temp4', 'active_alarm_count', 'alarm_name'])

def test0():
    w1 = writer.Writer()
    w1.write(Values_tuple(**send_tuple_dict))

test0()