#Nama   : Zidan Khoirul Rizki
#NIM    : 210511049
#Kelas  : R2
#Matkul : Pemrogaman Berorientasi Objek 2 

class Celcius:

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5

mycelcius = 63
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print(myfahrenheit)