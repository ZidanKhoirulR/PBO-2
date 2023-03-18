#Nama   : Zidan Khoirul Rizki
#NIM    : 210511049
#Kelas  : R2
#Matkul : Pemrogaman Berorientasi Objek 2 

class KonversiSuhu :

    def __init__(self, reamur):
        self.reamur = reamur

    def to_celcius(self):
        return (5/4) * self.reamur

    def to_fahrenheit(self):
        return (9/4) * self.reamur

    def to_kelvin(self):
        return (5/4) * self.reamur + 273.15

suhu = KonversiSuhu(75)
celcius = suhu.to_celcius()
fahrenheit = suhu.to_fahrenheit()
kelvin = suhu.to_kelvin()

# Konversi suhu 75 derajat Reamur ke Celcius
print(f"Konversi suhu {suhu.reamur} derajat reamur adalah {celcius} derajat celcius") # Output: 93.75

# Konversi suhu 75 derajat Reamur ke Fahrenheit
print(f"Konversi suhu {suhu.reamur} derajat reamur adalah {fahrenheit} derajat fahrenheit") # Output: 168.75

# Konversi suhu 75 derajat Reamur ke Kelvin
print(f"Konversi suhu {suhu.reamur} derajat reamur adalah {kelvin} derajat kelvin") # Output: 366.9