from abc import ABC, abstractmethod

class InPengadonan(ABC):
    @abstractmethod
    def pengadonan(self): 
        pass

class InPemanggangan(ABC):
    @abstractmethod
    def pemanggangan(self): 
        pass

class InPengembangan(ABC):
    @abstractmethod
    def pengembangan(self):
        pass

class InTopping(ABC):
    @abstractmethod
    def topping(self): 
        pass

class ProdukRoti(ABC):
    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    def estimasi_profit(self, jumlah):
        return (self.harga_jual - self.biaya_produksi) * jumlah

    @abstractmethod
    def produksi(self): 
        pass

    @abstractmethod
    def tampilkan_produk():
        pass
    
class RotiManis(ProdukRoti,InPengadonan,InPengembangan,InPemanggangan ):
    def produksi(self):
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()

    def pengadonan(self):
        print("Proses pengadonan")

    def pengembangan(self):
        print("Proses pengembangan")

    def pemanggangan(self):
        print("Proses pemanggangan")

    def tampilkan_produk(self):
        print("ROTI MANIS")
        print(f"Nama\t\t\t: {self.nama}")
        print(f"Kode Produk\t\t: {self.kode}")
        print(f"Bahan Baku\t\t: {','.join(self.bahan_baku)}")
        print(f"Biaya Produksi\t\t: Rp {self.biaya_produksi}")
        print(f"Harga Jual\t\t: Rp {self.harga_jual}")
        print(f"Estimasi Profit per unit: Rp {self.harga_jual - self.biaya_produksi}")
        print("")


class Croissant(ProdukRoti,InPengadonan,InPengembangan,InPemanggangan):
    def produksi(self):
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()

    def pengadonan(self):
        print("Proses pengadonan")

    def pengembangan(self):
        print("Proses pengembangan")

    def pemanggangan(self):
        print("Proses pemanggangan")

    def tampilkan_produk(self):
        print("CROISSANT")
        print(f"Nama\t\t\t: {self.nama}")
        print(f"Kode Produk\t\t: {self.kode}")
        print(f"Bahan Baku\t\t: {','.join(self.bahan_baku)}")
        print(f"Biaya Produksi\t\t: Rp {self.biaya_produksi}")
        print(f"Harga Jual\t\t: Rp {self.harga_jual}")
        print(f"Estimasi Profit per unit: Rp {self.harga_jual - self.biaya_produksi}") 
        print("")
       

class ButterCookies(ProdukRoti,InPengadonan,InPemanggangan,InTopping):
    def produksi(self):
        self.pengadonan()
        self.pemanggangan()
        self.topping()

    def pengadonan(self):
        print("Proses pengadonan")

    def pemanggangan(self):
        print("Proses pemanggangan")

    def topping(self):
        print("Menambahkan topping")

    def tampilkan_produk(self):
        print("BUTTER COOKIES")
        print(f"Nama\t\t\t: {self.nama}")
        print(f"Kode Produk\t\t: {self.kode}")
        print(f"Bahan Baku\t\t: {','.join(self.bahan_baku)}")
        print(f"Biaya Produksi\t\t: Rp {self.biaya_produksi}")
        print(f"Harga Jual\t\t: Rp {self.harga_jual}")
        print(f"Estimasi Profit per unit: Rp {self.harga_jual - self.biaya_produksi}")
        print("")


class Muffin(ProdukRoti,InPengadonan,InPengembangan,InPemanggangan,InTopping):

    def produksi(self):
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()
        self.topping()

    def pengadonan(self):
        print("pengadonan")

    def pengembangan(self):
        print("Proses pengembangan")

    def pemanggangan(self):
        print("Proses pemanggangan")

    def topping(self):
        print("Menambahkan topping")
    def tampilkan_produk(self):
        print("MUFFIN")
        print(f"Nama\t\t\t: {self.nama}")
        print(f"Kode Produk\t\t: {self.kode}")
        print(f"Bahan Baku\t\t: {','.join(self.bahan_baku)}")
        print(f"Biaya Produksi\t\t: Rp {self.biaya_produksi}")
        print(f"Harga Jual\t\t: Rp {self.harga_jual}")
        print(f"Estimasi Profit per unit: Rp {self.harga_jual - self.biaya_produksi}")
        print("")



def buat_produk(jenis, nama, kode, bahan, biaya, harga):
    produk_map = {
        "1": RotiManis,
        "2": Croissant,
        "3": ButterCookies,
        "4": Muffin
    }

    produk_class = produk_map.get(jenis)
    if not produk_class:
        raise ValueError("Jenis produk tidak valid")
    return produk_class(nama, kode, bahan, biaya, harga)