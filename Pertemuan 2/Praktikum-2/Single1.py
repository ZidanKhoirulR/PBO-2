# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("")


class Dog(Animal):

    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def speak(self):
        print("Woof!")


my_dog = Dog("Fido", "Labrador")
print("Name:", my_dog.name)
print("Breed:", my_dog.breed)
my_dog.speak()