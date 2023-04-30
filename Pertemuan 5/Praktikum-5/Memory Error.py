# 10

import numpy as np

try:
    arr = np.zeros((10000000, 10000000))  # Membuat array yang terlalu besar
except MemoryError:
    print("Terjadi kesalahan: program mencoba menggunakan lebih banyak memori daripada yang tersedia di sistem.")
