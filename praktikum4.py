import random

def latihan_pertama():
    list_ariel = []

    jumlah_angka = int(input("Masukkan jumlah angka yang ingin dimasukkan: "))

    for i in range(jumlah_angka):
        list_ariel.append(random.randint(1,10))

    print('=========[LATIHAN-1]=========')
    print("List1: " + ":", list_ariel)

latihan_pertama()


def latihan_kedua():
    nim = int(input("Masukkan dua digit terakhir NIM praktikan: "))
    list_awal.insert(0,nim)
    print('list baru:', list_awal)

print('=========[LATIHAN-2]=========')
list_awal = [4, 5, 9, 9, 17, 23, 28]
print('\n',list_awal)
latihan_kedua()



def latihan_ketiga():
    list_awal = [6, 5, 4, 2, 8]
    list_baru = [10, 20, 30, 40, 50]

    list_baru.extend(list_awal)

    print("List setelah digabungkan:", list_baru)

print('=========[LATIHAN-3]=========')
latihan_ketiga()



