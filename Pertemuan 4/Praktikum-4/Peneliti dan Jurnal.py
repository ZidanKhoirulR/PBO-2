# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2

class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
        self.artikel = []

    def tambah_artikel(self, judul, isi):
        artikel_baru = Artikel(judul, isi, self.bidang)
        self.artikel.append(artikel_baru)

    def kirim_ke_jurnal(self, jurnal):
        for artikel in self.artikel:
            jurnal.tambah_artikel(artikel)
        self.artikel = []


class Jurnal:
    def __init__(self, nama):
        self.nama = nama
        self.artikel = []

    def tambah_artikel(self, artikel):
        self.artikel.append(artikel)

    def tampilkan_artikel(self):
        print(f"Jurnal {self.nama}:")
        for artikel in self.artikel:
            print(f"Judul: {artikel.judul}")
            print(f"Isi: {artikel.isi}")
            print(f"Bidang: {artikel.bidang}")
            print("-----------")


class Artikel:
    def __init__(self, judul, isi, bidang):
        self.judul = judul
        self.isi = isi
        self.bidang = bidang


peneliti1 = Peneliti("Prof. Dr. Ir. Muhammad Yusuf, M.Sc.", "Sistem Informasi")
peneliti1.tambah_artikel(
    "Pengembangan Aplikasi Berbasis Augmented Reality untuk Peningkatan Pembelajaran di Sekolah Dasar", "Kami menemukan bahwa...")
peneliti1.tambah_artikel(
    "Sistem Pengaturan Pencahayaan Ruangan Berbasis Android Pada Rumah Pintar", "Dalam penelitian ini, kami...")
jurnal1 = Jurnal("Sistem Informasi")
peneliti1.kirim_ke_jurnal(jurnal1)
jurnal1.tampilkan_artikel()
