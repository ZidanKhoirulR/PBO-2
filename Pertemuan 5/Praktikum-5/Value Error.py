# 7

try:
    # Akan memicu ValueError karena string "abc" tidak bisa dikonversi menjadi bilangan bulat
    nilai = int("abc")
except ValueError:
    print("Terjadi kesalahan: nilai yang dimasukkan bukan bilangan bulat.")
