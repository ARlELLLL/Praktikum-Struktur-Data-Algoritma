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
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        balance = self.balance(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert_node(self, key):
        self.root = self.insert(self.root, key)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)
        if not node:
            return node

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        balance = self.balance(node)

        if balance > 1 and self.balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def delete_node(self, key):
        self.root = self.delete(self.root, key)

    def print_tree(self, node, prefix="", is_left=True):
        if node is not None:
            print(prefix, ("L----" if is_left else "R----"), "(", node.key, ")", sep="")
            self.print_tree(node.left, prefix + ("|    " if is_left else "     "), True)
            self.print_tree(node.right, prefix + ("|    " if is_left else "     "), False)

def menu(avl_tree):
    while True:
        print("Menu:")
        print("1. Insert node")
        print("2. Delete node")
        print("3. Close")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            key = int(input("Enter the key to insert: "))
            avl_tree.insert_node(key)
            avl_tree.print_tree(avl_tree.root)
        elif choice == 2:
            key = int(input("Enter the key to delete: "))
            avl_tree.delete_node(key)
            avl_tree.print_tree(avl_tree.root)
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

avl_tree = AVLTree()
digits = [3, 1, 13, 4, 5, 14]
for digit in digits:
    avl_tree.insert_node(digit)
avl_tree.print_tree(avl_tree.root)
menu(avl_tree)
