import controller

def main():
    while True:
        print("")
        print(f"{'==== SISTEM PRODUKSI HANARY BAKERY ====':^40}")
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulasi Estimasi Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            controller.tambah_produk()
        elif pilihan == "2":
            controller.tampilkan_produk()
        elif pilihan == "3":
            controller.estimasi_profit()
        elif pilihan == "4":
            controller.simulasi_produksi()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()
