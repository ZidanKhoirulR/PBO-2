def my_function():
    raise NotImplementedError("Fungsi belum diimplementasikan.")


try:
    my_function()
except NotImplementedError as e:
    print(e)
