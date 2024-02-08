import logging
import mysql.connector


logging.basicConfig(filename='gea_db_test.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

mydb = mysql.connector.connect(
    host="192.168.3.85",
    user="sa",
    password="sa",
    database="Energetika"
    )
logging.debug("connected")

def update():
    mycursor = mydb.cursor()
    sql = "UPDATE Energetika.values SET Utrip = %s, Pasica = %s, NovaPasica = %s, Kapaciteta = %s, GlikolVen = %s, GlikolNot = %s, VodaVen = %s, VodaNot = %s WHERE id = 1"
    val = (1, "kgsdh", 0, 0, 12.34, 22.34, 32.34, 42.34)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was updated.")

def select():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM frostlink.values")
    myresult = mycursor.fetchall()
    print(myresult)
