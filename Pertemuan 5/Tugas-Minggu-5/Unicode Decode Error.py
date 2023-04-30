try:
    b = b'\xc3\xb1'  # byte string dengan encoding utf-8
    s = b.decode('ascii')  # decode dengan format encoding yang salah
except UnicodeDecodeError as e:
    print(f"Error: {e}")
