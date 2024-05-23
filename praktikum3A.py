class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tambah(self, other):
        hasil_x = self.x + other.x
        hasil_y = self.y + other.y
        return Vector(hasil_x, hasil_y)

    def __str__(self):
        return f"({self.x}, {self.y})"

vektor1 = Vector(2, 10)
vektor2 = Vector(5, -2)

hasil_vektor = vektor1.tambah(vektor2)

print(f'''Vektor 1: {vektor1}
Vektor 2: {vektor2}
Hasil dari Vektor 1 + Vektor 2 adalah: Vektor {hasil_vektor}
''')
