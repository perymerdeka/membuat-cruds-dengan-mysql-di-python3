import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "fery123"
)

if db.is_connected():
    print("Berhasil terhubung")
else:
    print("coba lagi")
