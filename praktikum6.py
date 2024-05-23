import queue

class Queue:
    def __init__ (self):
        self.a = queue.Queue()

    def enqueue(self, data):
        self.a.put(data)
        print(f'Enqueue: {data} ')
    
    def dequeue(self):
        if not self.a.empty():
            data = self.a.get()
            print(f'Dequeue: {data}')
        else:
            print('Queue Kosong')
    
    def display(self):
        if not self.a.empty():
            print('Isi Queue: ')
            for data in list(self.a.queue):
                print(f'''[{data}], ''')

            
        else:
            print('Queue Kosong')
            
def main():
    obj = Queue()
    while True:
        print('''
--- Pilihan Menu ---
1. Enqueue
2. Dequeue
3. Tampilkan Queue
4. Keluar Program
        ''')
        
        pilihan = int(input('Pilih Menu: '))  

        if pilihan == 1:
            data = input('Masukkan item yang ditambahkan ke queue: ')
            obj.enqueue(data)
        elif pilihan == 2:
            obj.dequeue()
        elif pilihan == 3:
            obj.display()
        elif pilihan == 4:
            print("Terima kasih telah menggunakan program.")
            print('----------------')
            obj.display()
            break
        else:
            print('Error, karena nomor tidak ada di menu.')

main()






















'''
 queue_items = ', '.join([f"[{data}]" for data in list(self.a.queue)])
            print(queue_items)
'''