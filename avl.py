import random
import sys


def generate():
    n = random.randint(1000, 3000)
    m = random.randint(500, 1000)

    X = set()
    Y = set()

    for x in range(n):
        x = random.randint(-3000, 3000)
        X.add(x)

    for y in range(m):
        y = random.randint(-3000, 3000)
        Y.add(y)

    # print("Set X: \n", X)
    # print("Set Y: \n",  Y)
