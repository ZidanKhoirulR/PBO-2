def countdown(n):
    if n <= 0:
        return
    else:
        print(n)
        countdown(n-1)


try:
    countdown(10000)
except RecursionError as e:
    print("Terjadi kesalahan saat melakukan rekursi:", e)
