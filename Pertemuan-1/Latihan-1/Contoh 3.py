#Nama   : Zidan Khoirul Rizki
#NIM    : 210511049
#Kelas  : R2
#Matkul : Pemrogaman Berorientasi Objek 2 

class Lingkaran:

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * (self.jari_jari ** 2)
lingkaranA = Lingkaran(12)
print(f"Luas lingkaran: {lingkaranA.luas()}")