class Node:
    def __init__(self, name, id_number, address):
        self.name = name
        self.id_number = id_number
        self.address = address
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, name, id_number, address):
        new_node = Node(name, id_number, address)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, name, id_number, address):
        new_node = Node(name, id_number, address)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, name):
        temp = self.head
        if temp is not None:
            if temp.name == name:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.name == name:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(f'''
NAMA: {temp.name}
NIM: {temp.id_number}
Alamat: {temp.address}
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

    choice = int(input("Your choice? "))

    return choice

linked_list = LinkedList()

while True:
    option = menu()

    if option == 1:
        name = input("Enter name: ")
        id_number = input("Enter NIM: ")
        address = input("Enter address: ")
        linked_list.insert_at_beginning(name, id_number, address)
    elif option == 2:
        name = input("Enter name: ")
        id_number = input("Enter : ")
        address = input("Enter address: ")
        linked_list.insert_at_end(name, id_number, address)
    elif option == 3:
        name = input("Enter the name to be deleted: ")
        linked_list.delete_node(name)
    elif option == 4:
        linked_list.display()
    elif option == 5:
        break
    else:
        print("Invalid choice")
