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
        self.data = data  # Holds Key
        self.parent = None  # Pointer to Parent
        # Holds Left and Right of Children
        self.left = None
        self.right = None
        self.colour = True  # Where True is Red and False is Black


class Tree:

    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.colour = False
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

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

    def __search_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self.__search_helper(node.left, key)

        return self.__search_helper(node.right, key)

    def __delete_helper(self, x):
        while x != self.root and x.colour is False:
            if x == x.parent.left:
                y = x.parent.right
                if y.colour is True:

                    y.colour = False
                    x.parent.colour = True
                    self.leftrotate(x.parent)
                    y = x.parent.right

                if y.left.colour is False and y.right.colour is False:

                    y.colour = True
                    x = x.parent

                else:
                    if y.right.colour is False:

                        y.left.colour = False
                        y.colour = True
                        self.rightrotate(y)
                        y = x.parent.right

                    y.colour = x.parent.colour
                    x.parent.colour = False
                    y.right.colour = False
                    self.leftrotate(x.parent)
                    x = self.root

            else:

                y = x.parent.left
                if y.colour is True:

                    y.colour = False
                    x.parent.colour = True
                    self.rightrotate(x.parent)
                    y = x.parent.left

                if y.left.colour is False and y.right.colour is False:

                    y.colour = True
                    x = x.parent

                else:

                    if y.left.colour is False:

                        y.right.colour = False
                        y.colour = True
                        self.leftrotate(y)
                        y = x.parent.left

                    y.colour = x.parent.colour
                    x.parent.colour = False
                    y.left.colour = False
                    self.rightrotate(x.parent)
                    x = self.root

        x.colour = False

    def __redblack_refactor(self, x, y):

        if x.parent is None:
            self.root = y

        elif x == x.parent.left:
            x.parent.left = y

        else:
            x.parent.right = y

        y.parent = x.parent

    def __node_delete(self, node, key):

        #Finding Node containing the Key
        token = self.TNULL
        while node is not self.TNULL:
            if node.data == key:
                token = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

            if token is self.TNULL:
                print("Key does not exist")
                return

            y = token
            yc = y.colour
            if token.left is self.TNULL:
                x = token.right
                self.__redblack_refactor(token, token.right)

            else:
                y = self.minimum(token.right)
                yc = y.colour
                x = y.right

                if y.parent is token:
                    x.parent = y

                else:
                    self.__redblack_refactor(y, y.right)
                    y.right = token.right
                    y.right.parent = y

                self.__redblack_refactor(token, y)
                y.left = token.left
                y.left.parent = y
                y.colour = token.colour

            if yc is False:
                self.__delete_helper(x)


    def __insert_helper(self, x):

        while x.parent.colour is True:
            if x.parent is x.parent.parent.right:
                y = x.parent.parent.left

                if y.colour is True:

                    y.colour = False
                    x.parent.colour = False
                    x.parent.parent.colour = True
                    x = x.parent.parent

                else:
                    if x is x.parent.left:

                        x = x.parent
                        self.rightrotate(x)

                    x.parent.colour = False
                    x.parent.parent.colour = True
                    self.leftrotate(x.parent.parent)

            else:

                y = x.parent.parent.right

                if y.colour is True:

                    y.colour = False
                    x.parent.colour = False
                    x.parent.parent.colour = True
                    x = x.parent.parent

                else:
                    if x is x.parent.right:

                        x = x.parent
                        self.leftrotate(x)

                    x.parent.colour = False
                    x.parent.parent.colour = True
                    self.rightrotate(x.parent.parent)

                if x is self.root:
                    break

        self.root.colour = False

    def __print_helper(self, node, indent, last):

        if node is not self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "    "
            else:
                sys.stdout.write("L----")
                indent += "|   "

            tempcolour = "RED" if node.colour is True else "BLACK"
            print(str(node.data) + "(" + tempcolour + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    # --- Traversals ---
    def preorder(self):
        self.__preorder_helper(self.root)

    def inorder(self):
        self.__inorder_helper(self.root)

    def postorder(self):
        self.__postorder_helper(self.root)

    def searchtree(self, x):
        return self.__search_helper(self.root, x)

    def minimum(self, node):
        while node.left is not self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right is not self.TNULL:
            node = node.right
        return node

    def child(self, x):

        if x.right is not self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y is not self.TNULL and x is y.right:
            x = y
            y = y.parent

        return y

    def father(self, x):

        if x.left is not self.TNULL:
            return self.maximum(x.left)

        y = x.parent
        while y is not self.TNULL and x is y.left:
            x = y
            y = y.parent

        return y

    # --- Rotations ---

    def leftrotate(self, x):

        counter = 0

        y = x.right
        x.right = y.left
        if y.left is not self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

        counter += 1

    def rightrotate(self, x):

        counter = 0
        y = x.left
        x.left = y.right
        if y.right is not self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

        counter += 1

    def insert(self, key):

        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.colour = True #New node must be red

        y = None
        x = self.root

        while x is not self.TNULL:

            y = x
            if node.data < x.data:
                x = x.left

            else:
                x = x.right

            node.parent = y

            if y is None:
                self.root = node

            elif node.data < y.data:
                y.left = node

            else:
                y.right = node

            if node.parent is None:
                node.colour = False
                return

            if node.parent.parent is None:
                return

            self.__insert_helper(node)

    def getRoot(self):
        return self.root

    def delete(self, data):
        self.__node_delete(self.root, data)

    def printer(self):
        self.__print_helper(self.root, "", True)


if __name__ == "__main__":
    rbt = Tree()

    a = []
    b = []

    generate(a, b)

    print("Inserting from Set A\n")
    for x in range(a.__len__()):
        rbt.insert(a[x])

    rbt.printer()

    print("Deleting from Set Y\n")
    for y in range(b.__len__()):
        rbt.delete(b[y])

    rbt.printer()

    print("Process Complete")

