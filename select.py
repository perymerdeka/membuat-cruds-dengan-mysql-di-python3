import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "fery123",
    database = "toko_buku"
)

cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)
result = cursor.fetchall()

for data in result:
    print(data)