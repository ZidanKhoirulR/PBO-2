# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"This is a {self.brand} {self.model}")


class Car(Vehicle):

    def __init__(self, brand, model, num_of_doors):
        super().__init__(brand, model)
        self.num_of_doors = num_of_doors

    def info(self):
        super().info()
        print(f"It has {self.num_of_doors} doors")


my_car = Car("Toyota", "Corolla", 4)
my_car.info()  # Output: This is a Toyota Corolla. It has 4 doors.