import random
from enum import Enum
import sys

sys.setrecursionlimit(3001)

#GENERATING THE SETS

#Setting Set X
n = random.randint(1000,3000)
print("\nn: " ,n)
X = set(random.sample(range(-3000,3000), n))
print(len(X))

#Setting Set Y
m = random.randint(500,1000)
print("\nm: ", m)
Y = set(random.sample(range(-3000,3000), m))
print(len(Y))

#Setting Set Z
k = random.randint(1000, 2000)
print("\nk: ", k)
Z = set(random.sample(range(-3000, 3000), k))
print(len(Z))

#Determining Common Variables
intersection = X.intersection(Y)
print("\nSets X and Y have %d elements in common" % len(intersection))

#AVL TREE
class AVL_NODE(object):
    def __init__(self, content):
        self.content = content
        self.height = 1
        self.left = None
        self.right = None

class AVL(object):
    def __init__(self):
        self.nodes = 0
        self.comparisons = 0
        self.searches = 0
        self.rotations = 0

    #Returning Values 

    def retRotations(self):
        return self.rotations
    
    def retSearches(self):
        return self.searches

    def retCompares(self):
        return self.comparisons

    def retNodes(self, root):
        if not root:
            return 

        self.retNodes(root.left)
        self.nodes += 1
        self.retNodes(root.right)

    def retNodeCount(self, root):
        self.nodes = 0
        self.retNodes(root)
        return self.nodes

    def retMin(self, root):
        if root is None or root.left is None:
            return root

        return self.retMin(root.left)

    def retBalance(self, root):
        if not root:
            return 0
            #Left Subtree Height - Right Subtree Height
        return self.retHeight(root.left) - self.retHeight(root.right)


    #Traversals
    def preOrder(self, root):
    
        if not root:
            return

        print(root.content," ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):

        if not root:
            return

        self.inOrder(root.left)
        print(root.content," ", end="")
        self.inOrder(root.right)

    def postOrder(self, root):

        if not root:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.content," ", end="")

    #Rotation Functionality
    def leftrotate(self, x):
    
        #Update Counter
        self.rotations += 1
        y = x.right
        turn = y.left

        #Rotation
        y.left = x
        x.right = turn

        #Update Heights
        x.height = 1 + max(self.retHeight(x.left), self.retHeight(x.right))
        y.height = 1 + max(self.retHeight(y.left), self.retHeight(y.right))

        #New Root
        return y

    def rightrotate(self, x):

        #Update Counter
        self.rotations += 1
        y = x.left
        turn = y.right

        #Rotation
        y.right = x
        x.left = turn

        #Update Heights
        x.height = 1 + max(self.retHeight(x.left), self.retHeight(x.right))
        y.height = 1 + max(self.retHeight(y.left), self.retHeight(y.right))

        #New Root
        return y

    #INSERT FUNCTION
    def insert(self, root, content):

        self.comparisons += 1
        if not root:
            return AVL_NODE(content)
        elif content < root.content:
            root.left = self.insert(root.left, content)
        else:
            root.right = self.insert(root.right, content)

        #Parent Height
        root.height = 1 + max(self.retHeight(root.left), self.retHeight(root.right))

        balance = self.retBalance(root)

        #A balance larger than 1 implies an unbalanced tree and needs rotations

        #Rotating and Rebalancing
        #Left Left
        if balance > 1:
            if self.retBalance(root.left) >= 0:
                return self.rightrotate(root)

            #Left Right
            else:
                root.left = self.leftrotate(root.left)
                return self.rightrotate(root)

        #Right Right
        if balance < -1:
            if self.retBalance(root.right) <= 0:
                return self.leftrotate(root)

            #Right Left
            else:
                root.right = self.rightrotate(root.right)
                return self.leftrotate(root)

        return root

    #DELETE FUNCTION
    def delete(self, root, content):
    
        if not root:
            return root

        elif content < root.content:
            self.comparisons += 1
            root.left = self.delete(root.left, content)

        elif content > root.content:
            self.comparisons += 1
            root.right = self.delete(root.right, content)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.retMin(root.right)
            root.content = temp.content
            root.right = self.delete(root.right, temp.content)

        if root is None:
            return root

        root.height = 1 + max(self.retHeight(root.left), self.retHeight(root.right))

        balance = self.retBalance(root)

        #Rebalancing the Tree under the same conditions as insertion

        #Left Left
        if balance > 1:
            if self.retBalance(root.left) >= 0:
                return self.rightrotate(root)

            #Left Right
            else:
                root.left = self.leftrotate(root.left)
                return self.rightrotate(root)

        #Right Right
        if balance < -1:
            if self.retBalance(root.right) <= 0:
                return self.leftrotate(root)

            #Right Left
            else:
                root.right = self.rightrotate(root.right)
                return self.leftrotate(root)

        return root

    #SEARCH FUNCTION
    def search(self, root, content):
        self.searches += 1

        if root is None:
            return False

        elif root.content == content:
            return True

        elif root.content < content:
            return self.search(root.right, content)

        return self.search(root.left, content)

    def retHeight(self, root):
        if not root:
            return 0

        return root.height

#PRINTER
def printer(root, indent):

    tab = 4

    if root is None:
        return 

    indent = indent + tab

    printer(root.right, indent)

    for i in range(tab, indent):
        print(end=" ")
    print(root.content)

    printer(root.left, indent)

#RED BLACK TREE

class Colour(Enum):
    Black = 1
    Red = 2

class RBT_NODE():
    def __init__(self, content = None, colour = Colour.Red):
        self.right = None
        self.left = None
        self.parent = None
        self.content = content 
        self.colour = colour

class RBT:
    
    def __init__(self):
        self.NULL = RBT_NODE(content = None, colour = Colour.Black)
        self.root = self.NULL
        self.size = 0
        self.searches = 0
        self.height = 0
        self.rotations = 0
        self.comparisons = 0
        self.size = 0

    #Returing Values
    def retRotations(self):
        return self.rotations

    def retSearches(self):
        return self.searches

    def retSize(self):
        return self.size

    def retCompares(self):
        return self.comparisons

    #Minima and Maxima of Tree
    def maximum(self):
        if self.size == 0:
            return "Empty Tree"

        while self.root.right != self.NULL:
            self.root = self.root.right

        return self.root.content

    def minimum(self):
        if self.size == 0:
            return "Empty Tree"

        while self.root.left != self.NULL:
            self.root = self.root.left

        return self.root.content

    def minode(self, x):
        while x.left != self.NULL:
            x = x.left

        return x

    #Height 
    def retHeight(self, root):

        left_height = 0
        right_height = 0

        if root is None:
            return 0

        while root.right != self.NULL:
            root = root.right 
            right_height += 1

        while root.left != self.NULL:
            root = root.left
            left_height += 1

        if left_height >= right_height:
            self.height = left_height

        else:
            self.height = right_height

        return self.height

    #Traversals
    def preorder(self, root):
        if self.size == 0:
            print("Empty")
            return

        if root != self.NULL and root.content != None:
            print(root.content," ", end="")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if self.size == 0:
            print("Empty")
            return

        if root != self.NULL and root.content != None:
            self.inOrder(root.left)
            print(root.content," ", end="")
            self.inorder(root.right)

    def postorder(self, root):
        if self.size == 0:
            print("Empty")
            return

        if root != self.NULL and root.content != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.content," ", end="")

    #Rotations
    def leftrotate(self, x):

        #Incrementing Rotation Counter
        self.rotations += 1

        y = x.right
        x.right = y.left

        if y.left != self.NULL:
            y.left.parent = x 

        y.parent = x.parent

        if x.parent == self.NULL:
            self.root = y

        elif x == x.parent.left:
            x.parent.left = y 

        else:
            x.parent.right = y 

        y.left = x 
        x.parent = y 

    #In Reality, simply substituting right for left and vice versa for the above
    def rightrotate(self, x):

        #Incrementing Rotation Counter 
        self.rotations += 1

        y = x.left
        x.left = y.right 

        if y.right != self.NULL:
            y.right.parent = x 

        y.parent = x.parent 

        if x.parent == self.NULL:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y 

        else:
            x.parent.left = y 
        
        y.right = x 
        x.parent = y  

    #Insertion 
    def insert_helper(self, x):
        i = 0

        while x.parent.colour == Colour.Red:
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y.colour == Colour.Red:
                    x.parent.colour = Colour.Black
                    y.colour = Colour.Black
                    x.parent.parent.colour = Colour.Red
                    x = x.parent.parent

                else:
                    if x==x.parent.right:
                        x = x.parent
                        self.leftrotate(x)
                    x.parent.colour = Colour.Black
                    x.parent.parent.colour = Colour.Red
                    self.rightrotate(x.parent.parent)

            else:
                y = x.parent.parent.left
                if y.colour == Colour.Red:
                    x.parent.colour = Colour.Black
                    y.colour = Colour.Black
                    x.parent.parent.colour = Colour.Red
                    x = x.parent.parent

                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.rightrotate(x)
                    
                    x.parent.colour = Colour.Black
                    x.parent.parent.colour = Colour.Red
                    self.leftrotate(x.parent.parent)

            i += 1
        
        self.root.colour = Colour.Black

    def insert(self, x):

        node = RBT_NODE(content=x)

        y = self.NULL
        z = self.root

        while z!= self.NULL:

            y = z
            self.comparisons += 1

            if node.content < z.content:
                z = z.left
            
            else:
                z = z.right

        node.parent = y

        if y == self.NULL:
            self.root = node

        elif node.content < y.content:
            y.left = node

        else:
            y.right = node

        node.left = self.NULL
        node.right = self.NULL
        node.colour = Colour.Red

        self.insert_helper(node)

        self.size += 1

    #Searching and Searching by Key
    def search(self, root, key):

        self.searches += 1

        if root == self.NULL:
            return "Root does not Exist!"

        elif key == root.content:
            return "Found"

        elif key < root.content:
            return self.search(root.left, key)

        else:
            return self.search(root.right, key)

    def key_search(self, root, key):

        self.comparisons += 1

        if root == self.NULL:
            return None

        elif key == root.content:
            return self.root

        elif key < root.content:
            return self.key_search(root.left, key)

        else:
            return self.key_search(root.right, key)

    def transplant(self, x, y):

        if x.parent == self.NULL:
            self.root = y 

        elif x == x.parent.left:
            x.parent.left = y 

        else:
            x.parent.right = y 
        
        y.parent = x.parent

    #Deletion
    def delete_helper(self, x):

        while x!= self.root and x.colour == Colour.Black:

            if x == x.parent.left:
                a = x.parent.right

                if a.colour == Colour.Red:
                    a.colour = Colour.Black

                    x.parent.colour = Colour.Red 
                    self.leftrotate(x.parent)

                    a = x.parent.right

                if a.left.colour == Colour.Black and a.right.colour == Colour.Black:
                    a.colour = Colour.Red
                    x = x.parent

                else:

                    if a.right.colour == Colour.Black:
                        a.left.colour = Colour.Black
                        a.colour = Colour.Red

                        self.rightrotate(a)
                        a = x.parent.right 

                    a.colour = x.parent.colour
                    x.parent.colour = Colour.Black
                    a.right.colour = Colour.Black 

                    self.leftrotate(x.parent)
                    x = self.root

            else:
                a = x.parent.left
                if a.colour == Colour.Red:
                    a.colour = Colour.Black 
                    x.parent.colour = Colour.Red

                    self.rightrotate(x.parent)
                    a = x.parent.left

                if a.right.colour == Colour.Black and a.left.colour == Colour.Black:
                    a.colour = Colour.Red
                    x = x.parent

                else:
                    if a.left.colour == Colour.Black:
                        a.right.colour = Colour.Black
                        a.colour = Colour.Red

                        self.leftrotate(a)
                        a = x.parent.left

                    a.colour = x.parent.colour
                    x.parent.colour = Colour.Black
                    a.left.colour = Colour.Black
                    
                    self.rightrotate(x.parent)
                    x = self.root

        x.colour = Colour.Black

    def delete(self, z):

        if self.size == 0:
            print("Empty Tree")
            return 

        node1 = self.key_search(self.root, z)
        w = node1
        if node1 == None:
            return 

        col = w.colour

        if node1.left == self.NULL:
            x = node1.right
            self.transplant(node1, node1.right)

        elif node1.right == self.NULL:
            x = node1.left 
            self.transplant(node1, node1.right)

        else:
            w = self.minode(node1.right)
            x = w.right

            if w.parent == node1:
                x.parent = w  

            else:

                self.transplant(w, w.right)
                w.right = node1.right 
                w.right.parent = w 

            self.transplant(node1, w)
            w.left = node1.left 
            w.left.parent = w 
            w.colour = node1.colour 

        if col == Colour.Black:
            self.delete_helper(x)

        self.size -= 1


if __name__ == '__main__':

    AVLTREE = AVL()
    Root = None

    RBTREE = RBT()

    for y in X:
        Root = AVLTREE.insert(Root, y)

    for i in X:
        RBTREE.insert(i)

    print("After Insertion\n")

    print("AVL {} Rotations, Height {}, Nodes {}, Comparisons {}".format(AVLTREE.retRotations(), AVLTREE.retHeight(Root), AVLTREE.retNodeCount(Root), AVLTREE.retCompares()))
    print("RBT {} Rotations, Height {}, Nodes {}, Comparisons {}".format(RBTREE.retRotations(), RBTREE.retHeight(RBTREE.root), RBTREE.retSize(), RBTREE.retCompares()))
    
    #Deletion 
    for i in Y:
        AVLTREE.delete(Root, i)

    for i in Y:
        RBTREE.delete(i)

    print("After Deletion\n")

    print("AVL {} Rotations, Height {}, Nodes {}, Comparisons {}".format(AVLTREE.retRotations(), AVLTREE.retHeight(Root), AVLTREE.retNodeCount(Root), AVLTREE.retCompares()))
    print("RBT {} Rotations, Height {}, Nodes {}, Comparisons {}".format(RBTREE.retRotations(), RBTREE.retHeight(RBTREE.root), RBTREE.retSize(), RBTREE.retCompares()))

    #Searching 
    for i in Z:
        AVLTREE.search(Root, i)

    for i in Z:
        RBTREE.search(RBTREE.root, i)

    print("After Searching\n")
    print("K Value: ", k)

    print("AVL: {} Total Comparisons".format(AVLTREE.retCompares()))
    print("RBT: {} Total Comparisons".format(RBTREE.retCompares()))



