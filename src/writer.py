from collections import namedtuple
import pyodbc
import logging

class Writer():
    def __init__(self):
        self.namedtuple_output = namedtuple('Values', ['message', 'capacity', 'temp1', 'temp2', 'temp3', 'temp4', 'active_alarm_count', 'alarm_name'])
        # Connection string
        self.server = 'TOGEA15' # Replace 'your_server_name' with your server name
        self.database = 'Energetika' # Replace 'your_database_name' with your database name
        self.username = 'sa' # Replace 'your_username' with your SQL Server username
        self.password = 'togea' # Replace 'your_password' with your SQL Server password

        #logging.debug(server, database, username, password)

        self.conn_str = f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        logging.debug(self.conn_str)
        logging.debug("Writer initialized")

    def write(self, namedtuple_input):
        logging.debug("Writer write ", namedtuple_input)
        """ following: send to DB, each value """

        def update():
            mycursor = self.mydb.cursor()
            sql = "UPDATE frostlink.values SET message = %s, capacity = %s, temp1 = %s, temp2 = %s, temp3 = %s, temp4 = %s, active_alarm_count = %s WHERE id = 1"
            val = (namedtuple_input.message, namedtuple_input.capacity, namedtuple_input.temp1, namedtuple_input.temp2, namedtuple_input.temp3, namedtuple_input.temp4, namedtuple_input.active_alarm_count)
            mycursor.execute(sql, val)
            self.mydb.commit()
            logging.debug(mycursor.rowcount, "was updated.")

        def select():
            mycursor = self.mydb.cursor()
            mycursor.execute("SELECT * FROM frostlink.values")
            myresult = mycursor.fetchall()
            for x in myresult:
                logging.debug(x)
        
        try:
            # Connect to the database
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()

            update_query = """
            UPDATE RafHA_Komun
            SET Utrip = ?,
            Pasica = ?,
            Kapaciteta = ?,
            GlikolVen = ?,
            GlikolNot = ?,
            VodaVen = ?,
            VodaNot = ?
            """

            Utrip = 1
            Pasica = 'new_value2'
            Kapaciteta = 1
            GlikolVen = 1
            GlikolNot = 1
            VodaVen = 1
            VodaNot = 1

            condition_value = 'condition_value'

            # Execute the update query
            #cursor.execute(update_query, (new_value1, new_value2, condition_value))
            self.cursor.execute(update_query, (namedtuple_input.message, namedtuple_input.capacity, namedtuple_input.temp1, namedtuple_input.temp2, namedtuple_input.temp3, namedtuple_input.temp4))

            # Commit the transaction
            self.conn.commit()

            '''row = self.cursor.fetchone()
            logging.debug(row)
            logging.debug(row[0])
            print(row[0])  # Print the result'''

        except Exception as e:
            print(f"Error: {str(e)}")
            logging.error(e)

        finally:
            # Close the connection
            if 'conn' in locals():
                self.conn.close()

        update()
        select()

       