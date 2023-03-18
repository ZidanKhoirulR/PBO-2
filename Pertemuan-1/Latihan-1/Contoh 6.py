#Nama   : Zidan Khoirul Rizki
#NIM    : 210511049
#Kelas  : R2
#Matkul : Pemrogaman Berorientasi Objek 2 

class Kalkulator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y

# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(9, 5)) # Output: 14
print(Kalkulator.subtract(16, 7)) # Output: 11

# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(4, 7)) # Output: 28
print(Kalkulator.divide(24, 4)) # Output: 6.0