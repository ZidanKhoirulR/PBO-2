#Nama   : Zidan Khoirul Rizki
#NIM    : 210511049
#Kelas  : R2
#Matkul : Pemrogaman Berorientasi Objek 2 

class PesawatTerbang:
    def __init__(self, hari, tanggal, maskapai, derpature, arrive, harga):
        self.hari = hari
        self.tanggal = tanggal
        self.maskapai = maskapai
        self.derpature = derpature
        self.arrive = arrive
        self.harga = harga

    def info(self):
        print(f"===========================\n           WAKTU           \n===========================")
        print(f"Hari : {self.hari}\nTanggal : {self.tanggal}\nMaskapai: {self.maskapai}")
        print(f"===========================\n       PEMBERANGKATAN       \n===========================")
        print(f"Derpature : {self.derpature}\nArrive : {self.arrive}\nHarga(Rp) : {self.harga}")
pesawatA = PesawatTerbang("Kamis", "10 Feburari 2023", "Lion Air", "Jakarta (11.40)", "Surabaya (13.00)", "373.000,00")
pesawatA.info()