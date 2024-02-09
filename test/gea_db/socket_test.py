import pyodbc

def sql_server_exists(server, username=None, password=None):
    try:
        # Connection string
        conn_str = f'DRIVER=SQL Server;SERVER={server};'

        # Add authentication if provided
        if username and password:
            conn_str += f'UID={username};PWD={password};'

        # Attempt to connect to the SQL Server
        pyodbc.connect(conn_str, timeout=5)  # Set a timeout for the connection attempt
        return True
    except pyodbc.OperationalError:
        return False

# Example usage
server_name = 'TOGEA15'  # Replace with the SQL Server instance hostname or IP address
username = 'sa'  # Replace with your SQL Server username, if needed
password = 'togea15'  # Replace with your SQL Server password, if needed

if sql_server_exists(server_name, username, password):
    print(f"The SQL Server instance {server_name} is reachable.")
else:
    print(f"The SQL Server instance {server_name} is not reachable.")
