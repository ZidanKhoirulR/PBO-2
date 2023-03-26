# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Vehicle:

    def __init__(self, name):
        self.name = name

    def start(self):
        print("Starting", self.name)


class Car(Vehicle):

    def __init__(self, name, color):
        Vehicle.__init__(self, name)
        self.color = color

    def drive(self):
        print("Driving", self.name, "in", self.color, "color")


class Sedan(Car):

    def __init__(self, name, color, brand):
        Car.__init__(self, name, color)
        self.brand = brand

    def model(self):
        print("This", self.name, "is a", self.brand, "model")


my_sedan = Sedan("Civic", "Black", "Honda")
my_sedan.start()
my_sedan.drive()
my_sedan.model()