import pyodbc

# Connection string
server = r'TOGEA15\SQLEXPRESS' # Replace 'your_server_name' with your server name
database = 'Energetika' # Replace 'your_database_name' with your database name
username = 'sa' # Replace 'your_username' with your SQL Server username
password = 'togea' # Replace 'your_password' with your SQL Server password

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Execute SQL query
    cursor.execute('SELECT @@version')
    row = cursor.fetchone()
    print(row[0])  # Print the result

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the connection
    if 'conn' in locals():
        conn.close()


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