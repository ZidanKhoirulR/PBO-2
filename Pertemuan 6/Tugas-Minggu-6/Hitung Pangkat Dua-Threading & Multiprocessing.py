import threading
import multiprocessing

# Fungsi untuk menghitung pangkat dua dari sebuah angka
def hitung_pangkat_dua(angka):
    return angka ** 2

# Daftar angka yang akan diproses secara konkuren
angka_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Fungsi untuk menjalankan pemrosesan dengan threading
def pemrosesan_threading():
    results = []
    threads = []

    for angka in angka_list:
        t = threading.Thread(target=lambda: results.append(hitung_pangkat_dua(angka)))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return results

# Fungsi untuk menjalankan pemrosesan dengan multiprocessing
def pemrosesan_multiprocessing():
    with multiprocessing.Pool() as pool:
        results = pool.map(hitung_pangkat_dua, angka_list)

    return results

# Menjalankan pemrosesan dengan threading
hasil_threading = pemrosesan_threading()
print("Hasil pemrosesan dengan threading:")
print(hasil_threading)

# Menjalankan pemrosesan dengan multiprocessing
hasil_multiprocessing = pemrosesan_multiprocessing()
print("Hasil pemrosesan dengan multiprocessing:")
print(hasil_multiprocessing)
