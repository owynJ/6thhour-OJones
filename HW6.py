#Name: Owyn Jones
#Class: 6th Hour
#Assignment: HW6



#1. Create a list with 9 different numbers inside.
numberList = [1, 10, 11, 100, 101, 110, 111, 1000, 1001]

#2. Sort the list from highest to lowest.
numberList.sort(reverse=True)

#3. Create an empty list.
emptyList = []

#4. Remove the median number from the first list and add it to the second list.
emptyList.append(numberList[4])
numberList.pop(4)

#5. Remove the first number from the first list and add it to the second list.
emptyList.append(numberList[0])
numberList.pop(0)

#6. Print both lists.
print(numberList)
print(emptyList)

#7. Add the two numbers in the second list together and print the result.
emptyListSum = sum(emptyList)
print(emptyListSum)

#8. Add the sum from #7 to the first list.
numberList.append(emptyListSum)

#9. Sort the first list from lowest to highest and print it.
numberList.sort()
print(numberList)