#Name: Owyn Jones
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random
from random import shuffle

#2. print "Hello World!"
print ("Hello World!")

#3. Create three different variables that each randomly generate an integer between 1 and 10
randInt1 = random.randint(1, 10)
randInt2 = random.randint(1, 10)
randInt3 = random.randint(1, 10)

#4. Print the three variables from #3 on the same line.
print(randInt1, randInt2, randInt3)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
randInt1 += 2
randInt2 -= 4
randInt3 *= 1.5

#6. Print each result from #5 on the same line.
print(randInt1, randInt2, randInt3)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
randList = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

#8. Sort the list in #7 and print it.
randList.sort()
print(randList)

#9. Add together the highest three numbers in the list from #7 and print the result.
sumRandList = randList[1] + randList[2] + randList[3]
print(sumRandList)

#10. Create a list with 5 names of other students in this class and print the list.
nameList = ["Nate", "Jerrell", "Owen", "Tucker", "Matthew"]
print(nameList)

#11. Shuffle the list in #10 and print the list again.
shuffle(nameList)
print(nameList)

#12. Print a random choice from the list of names from #10.
print(nameList[random.randint(0,4)])