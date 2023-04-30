# 2

try:
    nilai = 80
    total_nilai = 0
    # Akan memicu ZeroDivisionError karena tidak bisa membagi dengan nol
    persentase = (nilai / total_nilai) * 100
except ZeroDivisionError:
    print("Terjadi kesalahan: tidak bisa membagi dengan nol.")
