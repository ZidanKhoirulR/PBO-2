# 5

try:
    data = []
    elemen_pertama = data[0]  # Akan memicu IndexError karena list kosong
except IndexError:
    print("Terjadi kesalahan: index diluar rentang list.")
