import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "fery123"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE Toko_buku")
print("database berhasil dibuat")