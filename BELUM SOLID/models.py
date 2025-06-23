from abc import ABC, abstractmethod

class InterProduksi (ABC):
    @abstractmethod
    def pengadonan(self): pass

    @abstractmethod
    def pemanggangan(self): pass

    def pengembangan(self): pass
    def topping(self): pass


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
    def produksi(self): pass


class RotiManis(ProdukRoti, InterProduksi ):
    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual):
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual)

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
        print(f"{self.nama} ({self.kode}): Biaya {self.biaya_produksi}, Harga {self.harga_jual}, Bahan: {self.bahan_baku}")


class Croissant(ProdukRoti, InterProduksi ):
    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual):
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual)

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
        print(f"{self.nama} ({self.kode}): Biaya {self.biaya_produksi}, Harga {self.harga_jual}, Bahan: {self.bahan_baku}")


class ButterCookies(ProdukRoti, InterProduksi ):
    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual):
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual)

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
        print(f"{self.nama} ({self.kode}): Biaya {self.biaya_produksi}, Harga {self.harga_jual}, Bahan: {self.bahan_baku}")


class Muffin(ProdukRoti, InterProduksi ):
    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual):
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual)

    def produksi(self):
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()

    def pengadonan(self):
        print("pengadonan")

    def pengembangan(self):
        print("Proses pengembangan")

    def pemanggangan(self):
        print("Proses pemanggangan")

    def tampilkan_produk(self):
        print(f"{self.nama} ({self.kode}): Biaya {self.biaya_produksi}, Harga {self.harga_jual}, Bahan: {self.bahan_baku}")
