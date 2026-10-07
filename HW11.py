#Name: Owyn Jones
#Class: 6th Hour
#Assignment: HW11

import random

#1. Print "Hello World!"
print("Hello World")

#2. Create a list with three variables that each randomly generate a number between 1 and 100
randList = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]

#3. Print the list.
print(randList)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if randList[0] > randList[1] and randList[0] > randList[2]:
    greatest = randList[0]
    print(randList[0])
elif randList[1] > randList[0] and randList[1] > randList[2]:
    greatest = randList[1]
    print(randList[1])
else:
    greatest = randList[2]
    print(randList[2])

#5. Tie the result (the largest number) from #4 to a variable called "num".
num = greatest

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    print("Num is divisible by 2")
    if num % 3 == 0:
        print("Num is also divisible by 3")
elif num % 3 == 0:
    print("Num is divisible by 3")
else:
    print("Num is not divisible by 2 or 3")