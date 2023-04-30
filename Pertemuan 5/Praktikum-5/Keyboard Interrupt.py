# 9

import time

try:
    for i in range(10):
        print(i)
        time.sleep(1)  # Menunggu selama 1 detik
except KeyboardInterrupt:
    print("Program dihentikan oleh user.")
else:
    print("Selesai.")
