import timeit
import matplotlib.pyplot as plt

def calculate_time_complexity(data_size):
    avg_times = []

    for size in data_size:
        total_time = 0

        for _ in range(5):  # Lakukan 5 kali percobaan
            lyst = [i for i in range(size)]

            # Algoritma atau operasi yang ingin diukur time complexity-nya
            def algorithm():
                for i in range(len(lyst) - 1):
                    _ = abs(lyst[i + 1] - lyst[i])

            elapsed_time = timeit.timeit(algorithm, number=1000)  # Lakukan 1000 kali iterasi
            total_time += elapsed_time

        avg_time = total_time / 5  # Hitung rata-rata waktu dari 5 percobaan
        avg_times.append(avg_time)

    return avg_times

def plot_graph(data_size, times):
    plt.plot(times, data_size, marker='o', color='blue', markerfacecolor='red', linestyle='-', markersize=8)
    plt.xlabel('Time (s)')
    plt.ylabel('Data Size')
    plt.title('Time Complexity Analysis')
    plt.grid(True)
    plt.ticklabel_format(useOffset=False, style='plain')  # Menampilkan waktu tanpa notasi ilmiah
    plt.xticks(rotation=45)  # Mengatur label sumbu x agar dapat ditampilkan dengan baik
    plt.yticks([500, 1000, 1500, 2000, 2500])  # Menampilkan label sumbu y sesuai dengan data_size
    plt.show()

if __name__ == "__main__":
    data_size = [150, 300, 500, 700, 750, 1000, 1300, 1600, 2000, 2500]
    
    avg_times = calculate_time_complexity(data_size)

    print("Data Size\tAverage Time (s)")
    print("---------------------------")
    for size, avg_time in zip(data_size, avg_times):
        print(f"{size}\t\t{avg_time:.2f} s")

    plot_graph(data_size, avg_times)