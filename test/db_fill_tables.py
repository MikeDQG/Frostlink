import mysql.connector
from mysql.connector import errorcode
config = {
    'user': 'local',
    'password': 'bamt_prektikum',
    'host': 'localhost',
    'raise_on_warnings': True, 
    'database': 'frostlink'
}

try:
    mydb = mysql.connector.connect(**config)
    mycursor = mydb.cursor()
    #mycursor.execute("drop database frostlink;")
    #mycursor.execute("CREATE DATABASE frostlink")
    '''mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)
    '''
    ''' '''
    #mycursor.execute("CREATE TABLE values (id INT AUTO_INCREMENT PRIMARY_KEY, handshake INT NOT NULL, message VARCHAR(45), capacity INT NOT NULL, temp1 FLOAT(7, 4) NOT NULL, temp2 FLOAT(7, 4) NOT NULL, temp3 FLOAT(7, 4) NOT NULL, temp4 FLOAT(7, 4) NOT NULL, active_alarm_count INT NOT NULL);")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    mydb.close()