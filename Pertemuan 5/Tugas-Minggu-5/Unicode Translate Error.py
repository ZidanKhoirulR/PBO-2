try:
    s = "こんにちは"  # string dengan karakter unicode
    # mengubah string menjadi byte string dengan format encoding iso-8859-1
    s.encode('iso-8859-1')
except UnicodeTranslateError as e:
    print(f"Error: {e}")
