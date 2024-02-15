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
        logging.debug("Writer write ")
        logging.debug(namedtuple_input)

        def update():
            update_cursor = self.conn.cursor()
            
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
            UTRIP = 1

            logging.info(update_query)
            #condition_value = 'condition_value'

            update_cursor.execute(update_query, (UTRIP, namedtuple_input.message, namedtuple_input.capacity, namedtuple_input.temp1, namedtuple_input.temp2, namedtuple_input.temp3, namedtuple_input.temp4))
            #update_cursor.execute(update_query, (namedtuple_input.message))

            self.conn.commit()

            logging.debug("Rowcount")
            logging.debug(update_cursor.rowcount)
        
        def select_version():
            query_string = "SELECT @@version;"
            self.cursor.execute(query_string)
            logging.debug(query_string)
            verr = self.cursor.fetchone()
            print(verr)
            logging.info(verr)

        def select():
            select_cursor = self.conn.cursor()
            data = select_cursor.fetchall()
            try:
                for d in data:
                    logging.debug(d)
            except Exception as exec:
                logging.info(exec)
                logging.warning("DB selected data not a list")
                logging.debug(data)
        
        try:
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()

            #select_version()
            update()
            select()

        except Exception as e:
            print(f"Error: {str(e)}")
            logging.error(e)

        finally:
            # Close the connection
            if 'conn' in locals():
                self.conn.close()


       