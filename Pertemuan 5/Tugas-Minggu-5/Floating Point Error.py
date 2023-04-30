try:
    x = 10.0 / 0.0
    print(x)
except ZeroDivisionError:
    print("Terjadi kesalahan: pembagian dengan bilangan pecahan nol.")
