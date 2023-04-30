def fungsi():
    print(x)
    x = 10


try:
    fungsi()
except UnboundLocalError:
    print("Variabel lokal belum didefinisikan.")
