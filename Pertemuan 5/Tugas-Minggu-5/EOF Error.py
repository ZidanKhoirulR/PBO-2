try:
    x = int(input("Masukkan bilangan bulat: "))
    print(f"Input yang dimasukkan adalah {x}")
except EOFError:
    print("Terjadi kesalahan: program mencoba membaca input dari pengguna yang telah berakhir.")
except ValueError:
    print("Terjadi kesalahan: input yang dimasukkan harus berupa bilangan bulat.")
