import pyodbc
import logging

logging.basicConfig(filename='dbsrvrtst.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.info("Start")

# Connection string
server = 'TOGEA15' # Replace 'your_server_name' with your server name
database = 'Energetika' # Replace 'your_database_name' with your database name
username = 'sa' # Replace 'your_username' with your SQL Server username
password = 'togea' # Replace 'your_password' with your SQL Server password

#logging.debug(server, database, username, password)

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
logging.debug(conn_str)

print(input("input1: ")) # stoopid test

try:
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Execute SQL query
    '''cursor.execute("SELECT @@version;")'''
    cursor.execute("UPDATE RafHA_Komun SET Utrip = 1, Pasica = 'Remote   Off', NovaPasica = 1, Kapaciteta = 0, GlikolVen = 12.34, GlikolNot = 12.35, VodaVen = 12.35, VodaNot = 12.35 WHERE id = 1")
    
    '''row = cursor.fetchone()
    logging.debug(row)
    logging.debug(row[0])
    print(row[0])  # Print the result'''

except Exception as e:
    print(f"Error: {str(e)}")
    logging.error(e)

finally:
    # Close the connection
    if 'conn' in locals():
        conn.close()

logging.debug("Done")

"""
conn_str = (
    'Driver=TOGEA15;'
    'Server=P5GTTEH;'
    'Database=Energetika;'
    'Trusted_Connection=yes;'
    )
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
cursor.execute("SHOW TABLES")
'''while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.LastName)
'''
x = cursor.fetchall()
cnxn.close()
print(x)"""

print(input("input2: ")) # stoopid test #2