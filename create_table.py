import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "fery123",
    database = "Toko_buku"
)

cursor = db.cursor()
sql = """ CREATE TABLE pengunjung (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255)
  )
"""
cursor.execute(sql)
print("Tabel Pengunjung berhasil dibuat")