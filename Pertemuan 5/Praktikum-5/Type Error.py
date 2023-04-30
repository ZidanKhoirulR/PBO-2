# 1

try:
    def greeting(Zidan):
        print("Hello, " + Zidan)

    greeting()  # Akan memicu Type Error karena fungsi greeting membutuhkan 1 parameter, namun tidak diberikan
except TypeError:
    print("Terjadi kesalahan: fungsi greeting membutuhkan 1 parameter.")
