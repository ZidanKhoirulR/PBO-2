#Nama   : Zidan Khoirul Rizki
#NIM    : 210511049
#Kelas  : R2
#Matkul : Pemrogaman Berorientasi Objek 2 

class KonversiSuhu :

    def __init__(self, kelvin):
        self.kelvin = kelvin

    def to_celcius(self):
        return self.kelvin - 273.15

    def to_reamur(self):
        return 4/5 * (self.kelvin - 273)

    def to_fahrenheit(self):
        return 9/5 * (self.kelvin - 273.15) + 32

suhu = KonversiSuhu(75)
celcius = suhu.to_celcius()
reamur = suhu.to_reamur()
fahrenheit = suhu.to_fahrenheit()

# Konversi suhu 75 derajat Kelvin ke Celcius
print(f"Konversi suhu {suhu.kelvin} derajat kelvin adalah {celcius} derajat celcius") # Output: -198.14999999999998

# Konversi suhu 75 derajat Kelvin ke Reamur
print(f"Konversi suhu {suhu.kelvin} derajat kelvin adalah {reamur} derajat reamur") # Output: -158.4

# Konversi suhu 75 derajat Kelvin ke Fahrenheit
print(f"Konversi suhu {suhu.kelvin} derajat kelvin adalah {fahrenheit} derajat fahrenheit") # Output: -324.66999999999996