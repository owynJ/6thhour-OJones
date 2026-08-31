#Name: Owyn Jones
#Class: 6th Hour
#Assignment: HW4

#1. Print "Hello World!"
print("Hello World")

#2. import the 'math' library
import math

#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x = float(input("Give me a float "))
y = int(input("Give me an integer "))

#4. Create a variable with the value that is x and y added together.
sum = x + y

#5. Print the variable from #4.
print("Sum of x and y: ",sum)

#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
divide = sum / 3

#7. Print the variable from #6.
print("Quotient of sum and 3: ",divide)

#8. Create a variable with the value of the square root of y, then print the result.
squareRoot = math.sqrt(y)
print("Square root of y: ",squareRoot)

#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
rounded = round(x, 1)
print("x rounded: ",rounded)

#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
ceiling = math.ceil(x)
print("Ceiling of x: ",ceiling)

#11. Use the floor function to round x down to the nearest whole number. Print the result.
floor = math.floor(x)
print("Floor of x: ",floor)