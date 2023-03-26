#Nama   : Zidan Khoirul Rizki
#NIM    : 210511049
#Kelas  : R2
#Matkul : Pemrogaman Berorientasi Objek 2 

class KonversiSuhu :

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def to_celcius(self):
        return 5/9 * (self.fahrenheit - 32)

    def to_reamur(self):
        return 4/9 * (self.fahrenheit - 32)

    def to_kelvin(self):
        return 5/9 * (self.fahrenheit - 32)

suhu = KonversiSuhu(75)
celcius = suhu.to_celcius()
reamur = suhu.to_reamur()
kelvin = suhu.to_kelvin()

# Konversi suhu 75 derajat Fahrenheit ke Celcius
print(f"Konversi suhu {suhu.fahrenheit} derajat fahrenheit adalah {celcius} derajat celcius") # Output: 23.88888888888889

# Konversi suhu 75 derajat Fahrenheit ke Reamur
print(f"Konversi suhu {suhu.fahrenheit} derajat fahrenheit adalah {reamur} derajat reamur") # Output: 19.11111111111111

# Konversi suhu 75 derajat Fahrenheit ke Kelvin
print(f"Konversi suhu {suhu.fahrenheit} derajat fahrenheit adalah {kelvin} derajat kelvin") # Output: 23.88888888888889