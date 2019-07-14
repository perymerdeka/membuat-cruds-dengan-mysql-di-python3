import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "fery123",
    database = "toko_buku",

)

cursor = db.cursor()
sql = "DELETE FROM customers WHERE customer_id=%s"
val = (1, )
cursor.execute(sql, val)

db.connect()
print("{} data telah berhasil dihapus".format(cursor.rowcount))