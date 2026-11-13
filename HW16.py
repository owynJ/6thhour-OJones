#Name: Owyn Jones
#Class: 6th Hour
#Assignment: HW16


#1. import the "random" library
import random
import math
import time
import sys

#2. print "Hello World!"
print("Hello World")

#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))
c = int(input("Enter and another integer: "))
if c == 0:
    print("That won't work...")
    sys.exit()
#4. Add a and b together, then divide the sum by c. Print the result.
d = (a + b) / c
print(d)

#5. Round the result from #3 up or down, and then determine if it is even or odd.
round(d)
if d % 2 ==0:
    print("Even")
else:
    print("Odd")

#6. Create a list of five different random integers between 1 and 10.
randList = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]

#7. Print the 4th number in the list.
print(randList[3])

#8. Append another integer to the end of the list, also random from 1 to 10.
randList.append(random.randint(1, 10))

#9. Sort the list from lowest to highest and then print the 4th number in the list again.
randList.sort()
print(randList[3])

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i < 100:
    i += i
    print(i)

#11. Create a list containing the names of five other students in the classroom.
names = ["Nate", "Raphael", "Owen", "Misa", "Braylee"]

#12. Create a for loop that individually prints out the names of each student in the list.
for i in names:
    print(i)

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for i in range(0, 100):
    if i % 10 == 0 and i != 0:
        break
    print(i)

#14. Free space. Do something creative. :)
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
x = int(input("Enter a number: "))
if is_prime(x):
    print(x,"is prime...")
    time.sleep(1)
else:
    print(x,"is not prime...")
    time.sleep(1)
for i in range(x, x ** x):
    if is_prime(i):
        print(i,"is prime")