import math
import sys

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#y = int(input("Range min: "))
#x = int(input("Range max: "))
#if y > x:
    print("That's not how ranges work")
    sys.exit()
#print("Prime numbers:")
#for i in range(y, x + 1):
    if is_prime(i):
        print(i)


#for i in range(1, 100):
    print(i,"", end="")


def grid(xLength, yHeight):
    for i in range(yHeight):
        for i in range(xLength):
            print("[ ]", end="")
        print()
xLength = int(input("x length: "))
yHeight = int(input("y height: "))
grid(xLength, yHeight)
#def verticalLine(xCoord):
