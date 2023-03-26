class Mobil:

    def __init__(self, produk, merek, warna, tahun):
        self.produk = produk
        self.merek = merek
        self.warna = warna
        self.tahun = tahun

    def info(self):
        print(f"Mobil {self.produk} dengan merek {self.merek} berwarna {self.warna} keluaran tahun {self.tahun}")
mobilA = Mobil("Toyota", "Kijang Inova", "Hitam", "2018")
mobilA.info() 