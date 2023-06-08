import concurrent.futures

# Fungsi untuk menghitung pangkat dua dari sebuah angka
def hitung_pangkat_dua(angka):
    return angka ** 2

# Daftar angka yang akan diproses secara konkuren
angka_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Menggunakan ThreadPoolExecutor untuk menjalankan pemrosesan konkuren
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Membuat task untuk setiap angka dalam daftar
    tasks = [executor.submit(hitung_pangkat_dua, angka) for angka in angka_list]

    # Mendapatkan hasil pemrosesan
    hasil = [task.result() for task in concurrent.futures.as_completed(tasks)]

# Cetak hasil pemrosesan
for h in hasil:
    print(h)