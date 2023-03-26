# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Vehicle:

    def __init__(self, name):
        self.name = name

    def start(self):
        print("Starting", self.name)


class Engine:

    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def fuel(self):
        print("Using", self.fuel_type, "as fuel")


class Car(Vehicle, Engine):

    def __init__(self, name, fuel_type):
        Vehicle.__init__(self, name)
        Engine.__init__(self, fuel_type)


my_car = Car("Sedan", "Petrol")
my_car.start()
my_car.fuel()