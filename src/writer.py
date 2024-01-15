#import db_object
from collections import namedtuple

class Writer():
    def __init__(self):
        #self.db_object = db_object.DB_Object()
        print("Writer init")

    def write(self, namedtuple_input):
       print("Writer write ", namedtuple_input)
       """ following: send to DB, each value """
