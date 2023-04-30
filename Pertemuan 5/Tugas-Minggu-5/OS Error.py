import os

try:
    os.mkdir("/path/to/new/folder")
except OSError as e:
    print("Terjadi kesalahan saat membuat folder:", e)
