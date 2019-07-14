import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "fery123",
    database = "toko_buku"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
value = [
    ("feri", "jakarta"),
    ("tejo", "Bungu"),
    ("budiono", "Jepara"),
    ("sarman", "Jepang")
]

for val in value:
    cursor.execute(sql, val)
    db.commit()

print("{} data telah ditambahkan". format((len(value))))