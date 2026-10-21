#Name: Owyn Jones
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

import sys

unit = input("imperial or metric? ")
if unit != "imperial" and unit != "metric":
    print("Invalid unit")
    sys.exit()
height = float(input("How tall are you? "))
weight = float(input("How much do you weigh? "))

if unit == "imperial":
    height /= 3.281
if unit == "imperial":
    weight /= 2.205

BMI = weight / (height ** 2)
BMI = round(BMI, 1)
print("Your BMI is", BMI)
if BMI < 18.5:
    print("You are underweight")
elif BMI < 24.9:
    print("You are normal weight")
elif BMI < 29.9:
    print("You are overweight")
else:
    print("You are obese")