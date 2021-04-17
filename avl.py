import random
import sys

def generate(x, y):
    n = random.randint(1000, 3000)
    m = random.randint(500, 1000)

    for i in range(n):
        i = random.randint(-3000, 3000)
        x.append(i)

    for j in range(m):
        j = random.randint(-3000, 3000)
        y.append(j)

    # print("Set X: \n", X)
    # print("Set Y: \n",  Y)

    return False

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:

    def __print_helper(self, pointer, indent, last):

    def __pre_order_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(node.data + "")
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def __in_order_helper(self, node):
        if node != self.TNULL:
            self.__inorder_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__inorder_helper(node.right)

    def __post_order_helper(self, node):
        if node != self.TNULL:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            sys.stdout.write(node.data + " ")

    def insert(self, root, key):
        if not root:
            return Node(key)

        elif key < root.key:
            root.left = self.insert(root.left, key)

        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if key < root.left.key:
                return self.rightrotate(root)

            else:
                root.left = self.leftrotate(root.left)
                return self.rightrotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.leftrotate(root)

            else:
                root.right = self.rightrotate(root.right)
                return self.leftrotate(root)

        return root

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def delete(self, root, key):

    def leftrotate(self, x):

        return 0

    def righrotate(self, x):

        return 0

    def preorder(self):
        self.__preorder_helper(self.root)

    def inorder(self):
        self.__inorder_helper(self.root)

    def postorder(self):
        self.__postorder_helper(self.root)

if __name__ == "__main__":

    x, y = []

    generate(x, y)