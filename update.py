import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "fery123",
    database = "toko_buku"
)

cursor = db.cursor()
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
val = ("parlan", "lombok", 2)
cursor.execute(sql, val)

db.commit()
print("{} data diubah".format(cursor.rowcount))