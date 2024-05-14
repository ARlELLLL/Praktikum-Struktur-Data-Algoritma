import time

def algorithm(n):
    # Contoh algoritma sederhana
    result = sum(range(n))
    return result

# Meminta input dua digit terakhir dari NIM
nim_last_two_digits = int(input("Masukkan dua digit terakhir NIM: "))
N = 150 + nim_last_two_digits

# Memulai mengukur waktu eksekusi algoritma
start_time = time.time()

# Memanggil algoritma dengan ukuran data yang ditentukan
output = algorithm(N)

# Menghentikan pengukuran waktu eksekusi algoritma
end_time = time.time()

# Menghitung waktu yang diperlukan untuk algoritma
elapsed_time_algorithm = end_time - start_time

# Menampilkan angka dari 0 sampai 150 + dua digit terakhir NIM
print(f"Angka dari 0 sampai {N}:")
for i in range(0, N + 1, 10):
    line = ' '.join(str(j).rjust(3) for j in range(i, min(i + 10, N + 1)))
    print(line)

# Menghitung waktu keseluruhan program dalam prosesnya
elapsed_time_whole_program = end_time - start_time

# Menampilkan hasil waktu proses
print("Elapsed time for the algorithm: {:.6f} seconds".format(elapsed_time_algorithm))
print("Time stop: {:.6f} seconds".format(end_time))
print("Elapsed time for the whole program in process: {:.6f} seconds".format(elapsed_time_whole_program))
