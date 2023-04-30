try:
    s = b'\xff\xfe\x41\x00\x42\x00'  # byte string yang tidak valid
    s.decode('utf-8')  # decode byte string dengan format encoding utf-8
except UnicodeError as e:
    print(f"Error: {e}")
