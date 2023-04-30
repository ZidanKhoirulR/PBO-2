# 3

try:
    # Akan memicu FileNotFoundError karena file tidak ada
    with open("file_penduduk1980.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Terjadi kesalahan: file tidak ditemukan.")
