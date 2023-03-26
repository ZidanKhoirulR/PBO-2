# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):

    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def bark(self):
        print(self.name, "is barking")


class Pug(Dog):

    def __init__(self, name, breed, age):
        Dog.__init__(self, name, breed)
        self.age = age

    def sleep(self):
        print(self.name, "is", self.age, "years old and sleeping")


my_pug = Pug("Buddy", "Pug", 3)
my_pug.eat()
my_pug.bark()
my_pug.sleep()