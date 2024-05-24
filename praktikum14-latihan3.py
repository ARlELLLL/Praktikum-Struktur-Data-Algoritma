from collections import deque
import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def tambah_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))

    def hapus_vertex(self, v):
        if v in self.graph:
            del self.graph[v]
        for k in self.graph:
            self.graph[k] = [(neighbor, w) for neighbor, w in self.graph[k] if neighbor != v]

    def hapus_edge(self, u, v):
        if u in self.graph:
            self.graph[u] = [(neighbor, w) for neighbor, w in self.graph[u] if neighbor != v]

    def dfs_util(self, v, visited, result):
        visited.add(v)
        result.append(v)
        for neighbor, _ in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, result)

    def dfs(self, start):
        visited = set()
        result = []
        self.dfs_util(start, visited, result)
        print(f'Penelusuran DFS dimulai dari vertex {start}: -> {" -> ".join(result)}')

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        print(f'Penelusuran BFS dimulai dari vertex {start}: ', end='')

        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor, _ in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print(" -> ".join(result))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        print(f'Jarak terpendek dari vertex {start}:')
        for vertex in distances:
            print(f'Ke {vertex} : {distances[vertex]}')

    def tampilkan(self):
        print("REPRESENTASI GRAPH (ADJACENCY LIST):")
        for vertex in self.graph:
            print(f'{vertex} -> {self.graph[vertex]}')

# Fungsi untuk menjalankan menu
def menu():
    g = Graph()
    while True:
        print(f'''
Menu
1. Tambah Vertex
2. Tambah edge            
3. Hapus edge
4. Hapus vertex
5. Tampilkan graph
6. Lakukan DFS  
7. Lakukan BFS
8. Lakukan Dijkstra
9. Keluar
                          
''')
        pilihan = int(input("Pilih opsi: "))
        
        if pilihan == 1:
            v = input("Masukkan vertex: ")
            g.tambah_vertex(v)
        elif pilihan == 2:
            u = input("Masukkan vertex asal: ")
            v = input("Masukkan vertex tujuan: ")
            weight = int(input("Masukkan berat edge: "))
            g.tambah_edge(u, v, weight)
        elif pilihan == 3:
            u = input("Masukkan vertex asal: ")
            v = input("Masukkan vertex tujuan: ")
            g.hapus_edge(u, v)
        elif pilihan == 4:
            v = input("Masukkan vertex: ")
            g.hapus_vertex(v)
        elif pilihan == 5:
            g.tampilkan()
        elif pilihan == 6:
            start = input("Masukkan vertex awal untuk DFS: ")
            g.dfs(start)
        elif pilihan == 7:
            start = input("Masukkan vertex awal untuk BFS: ")
            g.bfs(start)
        elif pilihan == 8:
            start = input("Masukkan vertex awal untuk Dijkstra: ")
            g.dijkstra(start)
        elif pilihan == 9:
            break
        else:
            print("Pilihan tidak valid.")

menu()
