# 4

try:
    data = {'nama': 'John', 'umur': 30}
    # Akan memicu KeyError karena 'pekerjaan' tidak ada dalam kamus
    pekerjaan = data['pekerjaan']
except KeyError:
    print("Terjadi kesalahan: kunci tidak ditemukan dalam kamus.")
