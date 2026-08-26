# Name: Owyn J
# Class: 6th Hour
# Assignment: HW3


#1. Print "Hello World!"
print("Hello World")

#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.
intEx = 37
stringEx = "Words"
boolEx = True

#3. Print all three variables on the same print function (at the same time).
print(intEx, stringEx, boolEx)

#4. Create a variable that asks the user to input an integer.
inputedInt = int(input("Give me a number "))

#5. Add the integer variable from #2 with the integer from #4 and print the result.
sum2And4 = intEx + inputedInt
print("Your number plus 37 from earlier is:", sum2And4)

#6. Take the result from #5 and divide it by 2. Print the result.
fiveDividedBy2 = sum2And4 / 2
print("That number divided by 2 is:", fiveDividedBy2)

#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).
boolEx = False

#8. Print the value of the boolean variable.
print("That boolean is now:", boolEx)

#9. Create a variable with a number that contains decimals.
floatEx = 6.7
print("Guys", floatEx)

#10. Round the number from #9 up or down using the round function.
floatEx = round(floatEx)
print("I'm sorry, it's", floatEx, "now")
