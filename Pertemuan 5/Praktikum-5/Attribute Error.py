# 6

class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur


try:
    jane = Orang("Jane", 25)
    jane.kerja()  # Akan memicu AttributeError karena objek Orang tidak memiliki metode 'kerja'
except AttributeError:
    print("Terjadi kesalahan: objek tidak memiliki metode yang diminta.")
