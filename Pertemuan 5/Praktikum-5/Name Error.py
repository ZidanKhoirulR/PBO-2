# 8

try:
    # Akan memicu NameError karena fungsi 'kuadrat' belum didefinisikan
    print(kuadrat(5))
except NameError:
    print("Terjadi kesalahan: fungsi yang diminta belum didefinisikan.")
