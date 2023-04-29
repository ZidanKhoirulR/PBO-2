# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2

class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna


class Mobil(Kendaraan):
    def __init__(self, jenis, merk, warna, jumlah_roda):
        super().__init__(jenis, merk, warna)
        self.jumlah_roda = jumlah_roda


class Motor(Kendaraan):
    def __init__(self, jenis, merk, warna, kapasitas_mesin):
        super().__init__(jenis, merk, warna)
        self.kapasitas_mesin = kapasitas_mesin


class Pengemudi:
    def __init__(self, nama, kendaraan):
        self.nama = nama
        self.kendaraan = kendaraan

    def info_kendaraan(self):
        if isinstance(self.kendaraan, Mobil):
            return f"{self.nama} mengendarai mobil {self.kendaraan.merk} berwarna {self.kendaraan.warna}."
        elif isinstance(self.kendaraan, Motor):
            return f"{self.nama} mengendarai motor {self.kendaraan.merk} berwarna {self.kendaraan.warna}."
        else:
            return f"{self.nama} belum memiliki kendaraan."


mobil1 = Mobil("Sedan", "Toyota", "Hitam", 4)
motor1 = Motor("Sport", "Yamaha", "Merah", 150)

pengemudi1 = Pengemudi("Andi", mobil1)
pengemudi2 = Pengemudi("Budi", motor1)
pengemudi3 = Pengemudi("Caca", None)

# output: Andi mengendarai mobil Toyota berwarna Hitam.
print(pengemudi1.info_kendaraan())
# output: Budi mengendarai motor Yamaha berwarna Merah.
print(pengemudi2.info_kendaraan())
print(pengemudi3.info_kendaraan())  # output: Caca belum memiliki kendaraan.
