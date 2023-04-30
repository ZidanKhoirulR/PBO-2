try:
    s = "नमस्ते"  # string yang mengandung karakter non-ASCII
    b = s.encode('ascii')  # encode dengan format encoding yang salah
except UnicodeEncodeError as e:
    print(f"Error: {e}")
