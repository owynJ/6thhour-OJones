#Name: Owyn Jones
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World")

#1. Create a list with 5 strings containing 5 different names in it.
stringList = ["John", "Jimmy", "James", "Joe", "Jonathan"]

#2. Append a new name onto the Name List.
stringList.append("Jack")

#3. Print out the 4th name on the list.
print(stringList[3])

#4. Create a list with 4 different integers in it.
intList = [2, 5, 7, 11]

#5. Insert a new integer into the 2nd spot and print the new list.
intList.insert(1, 3)
print(intList)

#6. Sort the list from lowest to highest and print the sorted list.
intList.sort()
print(intList)

#7. Add the 1st three numbers on the sorted list together and print the sum.
intSum = intList[0] + intList[1] + intList[2]
print(intSum)

#8. Create a list with two strings, two integers, and two boolean values.
mixedList = ["Bob", "Bobby", 13, 17, True, False]

#9. Create a print statement that asks the user to input their own index value for the list on #8.
inputedIndex = int(input("Input index for the mixed list (1-6): "))
print(mixedList[inputedIndex - 1])