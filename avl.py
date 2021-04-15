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

    def __preorder_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(node.data + "")
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def __inorder_helper(self, node):
        if node != self.TNULL:
            self.__inorder_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__inorder_helper(node.right)

    def __postorder_helper(self, node):
        if node != self.TNULL:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            sys.stdout.write(node.data + " ")

    def insert(self, root, key):

    def delete(self, root, key):

    def leftrotate(self, x):

    def righrotate(self, x):

    def preorder(self):
        self.__preorder_helper(self.root)

    def inorder(self):
        self.__inorder_helper(self.root)

    def postorder(self):
        self.__postorder_helper(self.root)

if __name__ == "__main__":

    x, y = []

    generate(x, y)