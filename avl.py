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


class Tree:

    def __pre_order_helper(self, node):
        if node is not None:
            sys.stdout.write(node.data + "")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node is not None:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node is not None:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.stdout.write(node.data + " ")

    def printer(self, pointer, indent, last):
        if pointer is not None:
            sys.stdout.write(indent)

            if last:
                sys.stdout.write("R----")
                indent += "     "

            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(pointer.key)

            self.printer(pointer.left, indent, False)
            self.printer(pointer.right, indent, True)

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

        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, koey)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMin(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightrotate(root)

            else:
                root.left = self.leftrotate(root.left)
                return self.rightrotate(root)

        if balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftrotate(root)

            else:
                root.right = self.rightrotate(root.right)
                return self.leftrotate(root)

        return root

    def getMin(self, root):
        if root is None or root.left is None:
            return root

        return self.getMin(root.left)

    def leftrotate(self, x):

        y = x.right
        turn = y.left
        y.left = x
        x.right = turn

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def righrotate(self, x):

        y = x.left
        turn = y.right
        y.right = x
        x.left = turn

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y


if __name__ == "__main__":

    avl = Tree()

    a = []
    b = []

    generate(a, b)

    print("Inserting from Set A\n")
    for x in range(a.__len__()):
        avl.insert(a[x])

    avl.printer()

    print("Deleting from Set Y\n")
    for y in range(b.__len__()):
        avl.delete(b[y])

    avl.printer()

    print("Process Complete")