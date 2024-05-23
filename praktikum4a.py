import random

# Inisialisasi list di luar fungsi-fungsi
list_data = []

def latihan_pertama(list_ariel):
    print('=========[LATIHAN-1]=========')
    jumlah_angka = int(input("Masukkan jumlah angka yang ingin dimasukkan: "))

    for i in range(jumlah_angka):
        list_ariel.append(random.randint(1, 10))

    print("List1: ", list_ariel)

def latihan_kedua(list_awal):
    print('=========[LATIHAN-2]=========')
    nim = int(input("Masukkan dua digit terakhir NIM praktikan: "))
    list_awal.insert(0, nim)
    print('list baru:', list_awal)

def latihan_ketiga(list_awal):
    print('=========[LATIHAN-3]=========')
    list_baru = [10, 20, 30, 40, 50]
    list_awal.extend(list_baru)
    

    print("List setelah digabungkan:", list_awal)

def latihan_keempat(list_awal):
    print('=========[LATIHAN-4]=========')

    # Penjumlahan isi dalam list
    total = sum(list_awal)
    print("1. Penjumlahan isi dalam list")
    print(total)

    # Mencari apakah ada angka yang dobel
    print("2. Mencari apakah ada angka yang dobel")
    angka_cek = int(input("Input(angka yang ingin di cek?): "))
    jumlah_sama = list_awal.count(angka_cek)
    if jumlah_sama > 1:
        print(f"Jumlah angka {angka_cek} yang sama = {jumlah_sama}")
    else:
        print(f'tidak ada angka yang sama di {angka_cek}')

    # Mencari panjang list
    print("3. Mencari panjang list")
    print(len(list_awal))

    # Mencari index dari suatu angka
    print("4. Mencari index dari suatu angka")
    angka_cari = int(input("Input(angka yang dicari?): "))
    if angka_cari in list_awal:
        index = list_awal.index(angka_cari)
        print(f"Index angka {angka_cari} adalah: {index}")
    else:
        print(f"Angka {angka_cari} tidak ditemukan di dalam list.")

def latihan_kelima(list_awal):
    print('=========[LATIHAN-5]=========')
    # IMPLEMENTASI POP
    print("----1. IMPLEMENTASI POP ------")
    index_pop = int(input("Inputan: Indeks elemen yang di-pop: "))
    if index_pop < len(list_awal):
        pop_value = list_awal.pop(index_pop)
        print(f"{pop_value}\n{list_awal}")
    else:
        print("Indeks melebihi panjang list.")

    # IMPLEMENTASI DEL
    print("----2. IMPLEMENTASI DEL ------")
    index_del = int(input("Inputan: Indeks elemen yang dihapus (del): "))
    if index_del < len(list_awal):
        del list_awal[index_del]
        print(list_awal)
    else:
        print("Indeks melebihi panjang list.")

    # IMPLEMENTASI REMOVE (hardcoded)
    print("----3. IMPLEMENTASI REMOVE ------")
    remove_value = 20  # Hardcoded value yang akan dihapus
    if remove_value in list_awal:
        list_awal.remove(remove_value)
        print(list_awal)
    else:
        print(f"Angka {remove_value} tidak ditemukan di dalam list.")




latihan_pertama(list_data)
latihan_kedua(list_data)
latihan_ketiga(list_data)
latihan_keempat(list_data)
latihan_kelima(list_data)
