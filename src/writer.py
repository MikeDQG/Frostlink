from collections import namedtuple
import mysql.connector

class Writer():
    def __init__(self):
        self.namedtuple_output = namedtuple('Values', ['message', 'capacity', 'temp1', 'temp2', 'temp3', 'temp4', 'active_alarm_count', 'alarm_name'])
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="local",
            password="bamt_prektikum",
            database="frostlink"
            )
        print("Writer init")

    def write(self, namedtuple_input):
       #self.namedtuple_output = namedtuple_input
       #print("Writer write ", self.namedtuple_output)
       print("Writer write ", namedtuple_input)
       """ following: send to DB, each value """
       def insert():
            mycursor = self.mydb.cursor()
            sql = "INSERT INTO frostlink.values (handshake, message, capacity, temp1, temp2, temp3, temp4, active_alarm_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (1, namedtuple_input.message, namedtuple_input.capacity, namedtuple_input.temp1, namedtuple_input.temp2, namedtuple_input.temp3, namedtuple_input.temp4, namedtuple_input.active_alarm_count)
            mycursor.execute(sql, val)
            self.mydb.commit()
            print(mycursor.rowcount, "was inserted.")
       def update():
            mycursor = self.mydb.cursor()
            sql = "UPDATE frostlink.values SET message = %s, capacity = %s, temp1 = %s, temp2 = %s, temp3 = %s, temp4 = %s, active_alarm_count = %s WHERE id = 1"
            val = (namedtuple_input.message, namedtuple_input.capacity, namedtuple_input.temp1, namedtuple_input.temp2, namedtuple_input.temp3, namedtuple_input.temp4, namedtuple_input.active_alarm_count)
            mycursor.execute(sql, val)
            self.mydb.commit()
            print(mycursor.rowcount, "was updated.")
       def select():
           mycursor = self.mydb.cursor()
           mycursor.execute("SELECT * FROM frostlink.values")
           myresult = mycursor.fetchall()
           for x in myresult:
               print(x)
       #insert()
       update()
       select()

       