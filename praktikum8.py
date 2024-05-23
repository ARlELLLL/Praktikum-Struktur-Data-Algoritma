class Node:
    def __init__(self, nama, nim, alamat):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sisip_awal(self, nama, nim, alamat):
        new_node = Node(nama, nim, alamat)
        new_node.next = self.head
        self.head = new_node

    def sisip_akhir(self, nama, nim, alamat):
        new_node = Node(nama, nim, alamat)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def hapus_elemen(self, nama):
        temp = self.head
        if temp is not None:
            if temp.nama == nama:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.nama == nama:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def tampilkan(self):
        temp = self.head
        while temp:
            print(f'''
______________________________
Nama: {temp.nama}                       
NIM: {temp.nim}                         
AlAMAT : {temp.alamat}                  
______________________________          
''')
            temp = temp.next

def menu():
    print(f'''
1. Sisip di awal
2. Sisip di akhir
3. Hapus elemen
4. Tampilkan SLL
5. Exit      
''')

    menu = int(input("Menu? "))

    return menu

linked_list = LinkedList()

while True:
    pilihan = menu()

    if pilihan == 1:
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        alamat = input("Masukkan alamat: ")
        linked_list.sisip_awal(nama, nim, alamat)
    elif pilihan == 2:
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        alamat = input("Masukkan alamat: ")
        linked_list.sisip_akhir(nama, nim, alamat)
    elif pilihan == 3:
        nama = input("Masukkan nama yang akan dihapus: ")
        linked_list.hapus_elemen(nama)
    elif pilihan == 4:
        linked_list.tampilkan()
    elif pilihan == 5:
        break
    else:
        print("Menu salah")