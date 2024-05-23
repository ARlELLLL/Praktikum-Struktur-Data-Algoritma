class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sisip_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def sisip_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def tambahkan_setelah(self, x, data):
        if self.head is None:
            print("List kosong")
            return
        current = self.head
        while current:
            if current.data == x:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Elemen '{x}' tidak ditemukan")

    def tambahkan_sebelum(self, x, data):
        if self.head is None:
            print("List kosong")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        prev = None
        current = self.head
        while current:
            if current.data == x:
                new_node = Node(data)
                new_node.next = current
                prev.next = new_node
                return
            prev = current
            current = current.next
        print(f"Elemen '{x}' tidak ditemukan")

    def hapus_elemen(self, data):
        if self.head is None:
            print("List kosong")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print(f"Elemen '{data}' tidak ditemukan")

    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print()

def main():
    sll = LinkedList()
    while True:
        print(f'''
1. Sisip Di awal
2. Sisip Di Akhir
3. Tambahkan 'data' setelah elemem 'x'
4. Tambahkan 'data' sebelum elemen 'x'                
5. Hapus Elemen
6. Tampilkan SLL
7. Keluar
_____________________________________________
              ''')

        pilihan = int(input("Menu: "))

        if pilihan == 1:
            data = input("Masukkan elemen yang ingin diinput: ")
            sll.sisip_di_awal(data)
        elif pilihan == 2:
            data = input("Masukkan elemen yang ingin diinput: ")
            sll.sisip_di_akhir(data)
        elif pilihan == 3:
            data = input("Masukkan elemen yang ingin diinput: ")
            x = input("Setelah elemen: ")
            sll.tambahkan_setelah(x, data)
        elif pilihan == 4:
            data = input("Masukkan elemen yang ingin diinput: ")
            x = input("Setelah elemen: ")
            sll.tambahkan_sebelum(x, data)
        elif pilihan == 5:
            data = input("Masukkan elemen yang ingin dihapus: ")
            sll.hapus_elemen(data)
        elif pilihan == 6:
            sll.tampilkan()
        elif pilihan == 7:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
main()