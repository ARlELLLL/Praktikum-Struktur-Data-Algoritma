class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x
    
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and key < root.left.key:
            print("Balancing:", root.left.key, "->", root.key)
            return self.rotate_right(root)

        if balance < -1 and key > root.right.key:
            print("Balancing:", root.right.key, "->", root.key)
            return self.rotate_left(root)

        if balance > 1 and key > root.left.key:
            print("Balancing:", root.left.key, "->", root.key)
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.key:
            print("Balancing:", root.right.key, "->", root.key)
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def insert_node(self, key):
        self.root = self.insert(self.root, key)

    def pre_order_traversal(self, root, depth=0, child_dir=''):
        if not root:
            return
        print("  " * depth + f"{child_dir}({root.key})")
        self.pre_order_traversal(root.left, depth + 1, 'L')
        self.pre_order_traversal(root.right, depth + 1, 'R')

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.key, end=" ")

    def pre_order_traversal(self, root):
        if root:
            print(root.key, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def find(self, root, key):
        if not root:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.find(root.left, key)
        else:
            return self.find(root.right, key)

    def print_tree(self):
        print("AVL Tree Structure:")
        self.pre_order_traversal(self.root)
        print("\nPost-order Traversal:")
        self.post_order_traversal(self.root)
        print("\nPre-order Traversal:")
        self.pre_order_traversal(self.root)
        print()


avl_tree = AVLTree()

digits = [3, 1, 13, 4, 5, 14] 
for digit in digits:
    avl_tree.insert_node(digit)

avl_tree.print_tree()

search_key = int(input("Masukkan angka yang ingin Anda cari dalam AVL Tree: "))
if avl_tree.find(avl_tree.root, search_key):
    print(f"{search_key} ditemukan dalam AVL Tree")
else:
    print(f"{search_key} tidak ditemukan dalam AVL Tree")
