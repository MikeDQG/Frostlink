import writer
from collections import namedtuple
import logging
        
logging.basicConfig(filename='writer_test_1.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
print(input("press any key to start ")) # stoopid test

send_tuple_dict = {'message': 'Local    Running', 'capacity': 75, 'temp1': 22.84566222222222, 'temp2': 5.449184999999998, 'temp3': 3.379012222222223, 'temp4': 26.772223333333336, 'active_alarm_count': 0, 'alarm_name': None}
Values_tuple = namedtuple('Values', ['message', 'capacity', 'temp1', 'temp2', 'temp3', 'temp4', 'active_alarm_count', 'alarm_name'])

logging.debug(send_tuple_dict)

def test0():
    w1 = writer.Writer()
    logging.info("write")
    w1.write(Values_tuple(**send_tuple_dict))
    logging.info("written")

test0()
print(input("press any key to close")) # stoopid test #2