import mysql.connector
import os

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "fery123",
    database = "Toko_buku"
)

def insert_data(db):
    name = input("Masukan Nama : ")
    address = input("Masukan Alamat : ")
    val = (name, address)
    cursor = db.cursor()
    sql = "INSERT INTO pengunjung (name, address) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{}  Data Berhasil disimpan".format(cursor.rowcount))


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM pengunjung"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak Ada Data")
    else:
        for x in results:
            print(x)

def update_data(db):
    cursor = db.cursor()
    show_data(db)
    customers_id = input("Pilih ID Pelanggan : ")
    name = input("Nama Baru : ")
    address = input("Alamat Baru : ")

    sql = "UPDATE pengunjung SET name=%s, address=%s WHERE customer_id=%s"
    val = (name, address, customers_id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil di ubah".format(cursor.rowcount))


def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    customer_id = input("Pilih ID Pelanggan : ")
    sql ="DELETE FROM pengunjung WHERE customer_id=%s"
    val = (customer_id,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
    cursor = db.cursor()
    keyword = input("Masukan Kata Kunci : ")
    sql = "SELECT * FROM pengunjung WHERE name LIKE %s OR address LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    hasil = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada Data")
    else:
        for data in hasil:
            print(data)


def show_menu(db):
    print("========== DAFTAR PENGUNJUNG PERPUSTAKAAN ===============")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari / Search Data")
    print("0. Keluar Aplikasi")
    print("-----------------------------------------------------------")
    menu = input("Pilih Menu > ")


    #clear Screen
    os.system("clear")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu Salah")


if __name__ == "__main__":
    while (True):
        show_menu(db)
