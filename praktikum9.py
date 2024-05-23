class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def preorder_traversal(root):
    if root:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')

def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right, key)
    return search(root.left, key)

def sort_elements(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root

def main ():
    data = [12, 5, 15, 3, 7, 13, 17, 1, 9]
    
    root = sort_elements(data)
    
    print("Preorder:")
    preorder_traversal(root)
    print()
    
    print("Postorder:")
    postorder_traversal(root)
    print()
    
    

    key = int(input("Cari angka? "))
    result = search(root, key)
    if result:
        print(f"{key} ditemukan dalam struktur data.")
    else:
        print(f"{key} Ga ditemukan.")

main()