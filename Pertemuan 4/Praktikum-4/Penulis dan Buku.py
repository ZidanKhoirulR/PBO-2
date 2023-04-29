# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2

class Penulis:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.buku = []

    def tambah_buku(self, judul):
        self.buku.append(Buku(judul))

    def info(self):
        print(f"Nama Penulis: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print("Buku yang ditulis:")
        for buku in self.buku:
            print("- " + buku.judul)
        print()


class Buku:
    def __init__(self, judul):
        self.judul = judul

    def info(self):
        print(f"Judul Buku: {self.judul}")


# membuat objek Penulis
penulis1 = Penulis("Andrea Hirata", "Indonesia")
penulis2 = Penulis("Arundhati Roy", "India")
penulis3 = Penulis("Orhan Pamuk", "Turki")

# menambahkan beberapa buku untuk penulis
penulis1.tambah_buku("Laskar Pelangi")
penulis1.tambah_buku("Sang Pemimpi")
penulis1.tambah_buku("Cinta Dalam Gelas")
penulis2.tambah_buku("The God of Small Things")
penulis3.tambah_buku("Snow")

# menampilkan informasi Penulis dan Buku
penulis1.info()
penulis2.info()
penulis3.info()
