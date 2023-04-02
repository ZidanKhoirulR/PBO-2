from playsound import *
import pygame
pygame.init()


class Animal:
    def __init__(self, suara_file):
        self.suara_file = suara_file

    def buat_Suara(self):

        pygame.mixer.music.load(self.suara_file)
        pygame.mixer.music.play()


class Kucing(Animal):
    def __init__(self):
        super().__init__('Sound/Cat.mp3')


class Anjing(Animal):
    def __init__(self):
        super().__init__('Sound/Dog.mp3')


class Sapi(Animal):
    def __init__(self):
        super().__init__('Sound/Cow.wav')


class Kuda(Animal):
    def __init__(self):
        super().__init__('Sound/Horse.mp3')


class Domba(Animal):
    def __init__(self):
        super().__init__('Sound/Sheep.mp3')


class Babi(Animal):
    def __init__(self):
        super().__init__('Sound/Pig.wav')


class Ayam(Animal):
    def __init__(self):
        super().__init__('Sound/Rooster.mp3')


class Bebek(Animal):
    def __init__(self):
        super().__init__('Sound/Duck.mp3')


class Gajah(Animal):
    def __init__(self):
        super().__init__('Sound/Elephant.mp3')


class Singa(Animal):
    def __init__(self):
        super().__init__('Sound/Lion.mp3')


kelas_hewan = [Kucing(), Anjing(), Sapi(), Kuda(), Domba(), Babi(),
               Ayam(), Bebek(), Gajah(), Singa()]

for hewan in kelas_hewan:
    print(hewan)

    hewan.buat_Suara()
    pygame.time.delay(3000)

pygame.quit()
