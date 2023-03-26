# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Shape:

    def __init__(self, color):
        self.color = color


class Fillable:

    def __init__(self, is_filled):
        self.is_filled = is_filled


class Square(Shape, Fillable):

    def __init__(self, side_length, color, is_filled):
        Shape.__init__(self, color)
        Fillable.__init__(self, is_filled)
        self.side_length = side_length
        
    def area(self):
        return self.side_length ** 2


my_square = Square(5, "red", True)
print("Side Length:", my_square.side_length)
print("Color:", my_square.color)
print("Filled:", my_square.is_filled)
print("Area:", my_square.area())