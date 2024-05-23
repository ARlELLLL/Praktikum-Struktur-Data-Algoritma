def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False
 
def add(stk,item):
    stk.append(item)
     
def remove(stk):
    if isEmpty(stk):
        print("Stack nya, ga ada isinya...")
    else:
        print("POP :",stk.pop())
     
def display(stk):
    if isEmpty(stk):
        print("Stack nya kosong... ")
    else :
        top = len(stk)-1
        print(stk[top])
        for a in range(top-1,-1,-1):
            print(stk[a])
             
stack=[]
top = None

print(f'''
STACK OPERATION:
1. PUSH
2. POP
3. TAMPILAN STACK
4. CLOSE
''')

while True:
    pilihan = int(input('Menu: '))

    if pilihan == 1 :
        item = input("Masukkan item yang ingin ditambahkan: ")
        add(stack, item)
    if pilihan == 2:
        remove(stack)
    if pilihan == 3:
        display(stack)
    if pilihan == 4:
        display(stack)
        break
