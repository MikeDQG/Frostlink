import pyodbc
import logging

logging.basicConfig(filename='db_any_query.log', filemode='a', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.info("Start")

# Connection string
server = 'TOGEA15' # Replace 'your_server_name' with your server name
database = 'Energetika' # Replace 'your_database_name' with your database name
username = 'sa' # Replace 'your_username' with your SQL Server username
password = 'togea' # Replace 'your_password' with your SQL Server password

#logging.debug(server, database, username, password)

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
logging.debug(conn_str)

print(input("press any key to start ")) # stoopid test

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    update_query = input("your query: ")

    logging.info(update_query)

    cursor.execute(update_query)

    conn.commit()


except Exception as e:
    print(f"Error: {str(e)}")
    logging.error(e)

finally:
    # Close the connection
    if 'conn' in locals():
        conn.close()

logging.debug("Done")

print(input("press any key to close")) # stoopid test #2