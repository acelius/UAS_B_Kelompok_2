from models import RotiManis, Croissant, Muffin, ButterCookies

produk_list = []

def tambah_produk():
    print(f"{'==== JENIS PRODUK ====':^40}")
    jenis = input("1.Roti Manis\n2.Croissant\n3.Butter Cookies\n4.Muffin\nProduk yang dipilih : ")
    nama = input("Nama Produk: ")
    kode = input("Kode Produk: ")
    bahan = input("Bahan Baku (pisahkan dengan koma): ").split(',')
    biaya = int(input("Biaya Produksi: "))
    harga = int(input("Harga Jual: "))

    if jenis == "1":
        produk = RotiManis(nama, kode, bahan, biaya, harga)
    elif jenis == "2":
        produk = Croissant(nama, kode, bahan, biaya, harga)
    elif jenis == "3":
        produk = ButterCookies(nama, kode, bahan, biaya, harga)
    elif jenis == "4":
        produk = Muffin(nama, kode, bahan, biaya, harga)
    else:
        print("Jenis tidak valid")
        return
    produk_list.append(produk)
    print("Produk berhasil ditambahkan!")

def tampilkan_produk():
    if not produk_list:
        print("Belum ada produk yang ditambahkan.")
        return
    print("\n=== Daftar Produk ===")
    for p in produk_list:
        p.tampilkan_produk()

def estimasi_profit():
    kode = input("Masukkan kode produk: ")
    jumlah = int(input("Jumlah pcs yang akan diproduksi: "))
    for p in produk_list:
        if p.kode == kode:
            print(f"Estimasi profit: Rp {p.estimasi_profit(jumlah)}")
            return
    print("Produk tidak ditemukan!")

def simulasi_produksi():
    kode = input("Masukkan kode produk: ")
    for p in produk_list:
        if p.kode == kode:
            print(f"Simulasi produksi untuk {p.nama}:")
            p.produksi()
            return
    print("Produk tidak ditemukan!")
