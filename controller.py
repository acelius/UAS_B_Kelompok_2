
from models import buat_produk

produk_list = []

def tambah_produk():
    print("")
    print(f"{'==== JENIS PRODUK ====':^40}")
    jenis = input("1.Roti Manis\n2.Croissant\n3.Butter Cookies\n4.Muffin\n\nProduk yang dipilih [1,2,3,4] : ")
    nama = input("Nama Produk\t: ")
    kode = input("Kode Produk\t: ")
    bahan = input("Bahan Baku\t: ").split(',')
    biaya = int(input("Biaya Produksi\t: "))
    harga = int(input("Harga Jual\t: "))

    try:
        produk = buat_produk(jenis, nama, kode, bahan, biaya, harga)
        produk_list.append(produk)
        print("Produk berhasil ditambahkan!")
    except ValueError as e:
        print("Produk gagal ditambahkan")

def tampilkan_produk():
    if not produk_list:
        print("Belum ada produk yang ditambahkan.")
        return
    print(f"{'==== DAFTAR PRODUK ====':^40}")
    for p in produk_list:
        p.tampilkan_produk()

def estimasi_profit():
    kode = input("Masukkan kode produk\t\t: ")
    jumlah = int(input("Jumlah pcs yang akan diproduksi\t: "))
    for p in produk_list:
        if p.kode == kode:
            print(f"Estimasi profit\t\t\t: Rp {p.estimasi_profit(jumlah)}")
            return
    print("Produk tidak ditemukan!")

def simulasi_produksi():
    kode = input("Masukkan kode produk: ")
    for p in produk_list:
        if p.kode == kode:
            print("")
            print(f"Simulasi Produksi {p.nama}:")
            p.produksi()
            return
    print("Produk tidak ditemukan!")
