# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Vehicle:

    def __init__(self, color):
        self.color = color

    def start(self):
        print("Starting vehicle...")


class Car(Vehicle):

    def __init__(self, color, make, model):
        Vehicle.__init__(self, color)
        self.make = make
        self.model = model

    def start(self):
        Vehicle.start(self)
        print("Starting car...")
        
    def stop(self):
        print("Stopping car...")


my_car = Car("blue", "Toyota", "Corolla")
print("Color:", my_car.color)
print("Make:", my_car.make)
print("Model:", my_car.model)
my_car.start()
my_car.stop()