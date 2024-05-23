class Karyawan:
    totalKaryawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.totalKaryawan += 1

    def displayEmployee(self):
        print("Name:", self.nama, ", Salary:", self.gaji)

    @classmethod
    def hitungTotalKaryawan(cls):
        return cls.totalKaryawan

Karyawan1 = Karyawan("ARIEL", 2000)
Karyawan2 = Karyawan("FEBRIO", 5000)
Karyawan3 = Karyawan("HADI", 5000)

Karyawan1.displayEmployee()
Karyawan2.displayEmployee()
Karyawan3.displayEmployee()

print ("Total Employee:", Karyawan.hitungTotalKaryawan())
