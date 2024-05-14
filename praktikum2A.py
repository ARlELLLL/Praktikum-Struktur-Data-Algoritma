import time
import matplotlib.pyplot as plt

# Fungsi dengan Quadratic Complexity
def quadratic_complexity(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

# List nilai n yang akan diuji
n_values = [10, 50, 100, 200]

# List untuk menyimpan waktu eksekusi
execution_times = []

# Mengukur waktu eksekusi untuk setiap nilai n
for n in n_values:
    start_time = time.time()
    quadratic_complexity(n)
    end_time = time.time()
    execution_times.append(end_time - start_time)

# Plot grafik
plt.plot(n_values, execution_times, marker='o')
plt.xlabel('Nilai n')
plt.ylabel('Waktu Eksekusi (s)')
plt.title('Grafik Quadratic Complexity')
plt.grid(True)
plt.show()
