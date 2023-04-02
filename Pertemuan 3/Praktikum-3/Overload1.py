# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2

class Vehicle:
    def __init__(self, distance, time):
        self.distance = distance
        self.time = time

    def calculate_speed(self):
        pass


class Car(Vehicle):
    def calculate_speed(self):
        return self.distance / self.time


class Bike(Vehicle):
    def calculate_speed(self):
        return self.distance / (self.time / 2)


class Train(Vehicle):
    def calculate_speed(self):
        return (self.distance * 1000) / (self.time * 3600)


car = Car(100, 2)
bike = Bike(50, 1)
train = Train(200, 3)

# Output: Kecepatan mobil: 50.0 km/jam
print("Kecepatan mobil:", car.calculate_speed(), "km/jam")
# Output: Kecepatan sepeda: 100.0 km/jam
print("Kecepatan sepeda:", bike.calculate_speed(), "km/jam")
# Output: Kecepatan kereta: 18.51851851851852 km/jam
print("Kecepatan kereta:", train.calculate_speed(), "km/jam")
