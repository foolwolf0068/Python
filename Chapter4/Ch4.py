# -*- coding: utf-8 -*-
"""
Created on Wed Sep  11 20:49:06 2019
@author: foolwolf0068
"""
'''
# 4.1
from math import sqrt
a, b, c = eval(input('Enter a, b, c: '))
delta = b*b-4*a*c
if(delta<0):
    print('The equation has no real roots')
elif(delta>0):
    r1 = 0.5*(-b+sqrt(delta))/a
    r2 = 0.5*(-b-sqrt(delta))/a
    print('The roots are {0:.6f} and {1:.6f}'.format(r1,r2))
else:
    r1 = -0.5*b/a
    print('The root is',r1)

# 4.2
from random import randint
num1 = randint(0,9)
num2 = randint(0,9)
num3 = randint(0,9)
answer2 = eval(input('What is '+str(num1)+' + '+str(num2)+' + '+str(num3)+' ? '))
print(num1,'+',num2,'+',num3,'=',answer2,
      'is',num1+num2+num3 == answer2)

# 4.3
a, b, c, d, e, f = eval(input('Enter a, b, c, d, e, f: '))
div = a*d - b*c
if(div != 0):
    x = (e*d - b*f)/div
    y = (a*f - e*c)/div
    print('x is {0:.1f} and y is {1:.1f}'.format(x, y))
else:
    print('The equation has no solution')

# 4.4
from random import randint
num1 = randint(0,99)
num2 = randint(0,99)
answer4 = eval(input('What is '+str(num1)+' + '+str(num2)+' ? '))
print(num1,'+',num2,'+','=',answer4,'is',num1+num2 == answer4)

# 4.5
week=['Sunday', 'Monday', 'Tursday', 'Wednsday', 'Thursday', 'Friday', 'Saturday']
today = eval(input('Enter today\'s day: '))
numday = eval(input('Enter the number of days elapsed since today: '))
thatday = (today + numday)%7
print('Today is',week[today],'and the future day is', week[thatday])

# 4.6
# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))
# Prompt the user to enter height in inches
height0 = eval(input('Enter feet: '))
height = eval(input("Enter height in inches: "))+height0*12

KILOGRAMS_PER_POUND = 0.45359237 # Constant
METERS_PER_INCH = 0.0254 # Constant

# Compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

# Display result
print("BMI is", format(bmi, ".15f"))
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")

# 4.7
# Receive the amount
amount = eval(input("Enter an amount, for example, 1156: "))
# Convert the amount to cents
remainingAmount = amount #int(amount * 100)
# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100
# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25
# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10
# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5
# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount
# Display the results
print("Your amount", amount, "consists of:")
if(numberOfOneDollars!=0):
    print("\t", numberOfOneDollars,end=' ')
    if(numberOfOneDollars==1):
        print("dollar")
    elif(numberOfOneDollars>=2):
        print("dollars")
if(numberOfQuarters!=0):
    print("\t", numberOfQuarters,end=' ')
    if(numberOfQuarters==1):
        print("quarter")
    elif(numberOfQuarters>=2):
        print("quarters")
if(numberOfDimes!=0):
    print("\t", numberOfDimes,end=' ')
    if(numberOfDimes==1):
        print("dime")
    elif(numberOfDimes>=2):
        print("dimes")
if(numberOfNickels!=0):
    print("\t", numberOfNickels,end=' ')
    if(numberOfNickels==1):
        print("nickel")
    elif(numberOfNickels>=2):
        print("nickels")
if(numberOfPennies!=0):
    print("\t", numberOfPennies,end=' ')
    if(numberOfPennies==1):
        print("penny")
    elif(numberOfPennies>=2):
        print("pennies")

# 4.8
num1 = eval(input('num1 = '))
num2 = eval(input('num2 = '))
num3 = eval(input('num3 = '))
num = [num1, num2, num3]
num.sort()
print(num)

#4.9
weight1, price1 = eval(input('Enter weight and price for package 1: '))
weight2, price2 = eval(input('Enter weight and price for package 2: '))
rate1 = price1/weight1
rate2 = price2/weight2
if(rate1<rate2):
    print('Package 1 has the better price.')
elif(rate1>rate2):
    print('Package 2 has the better price.')
else:
    print('Either of them is OK.')

# 4.10
import random

# 1. Generate two random single-digit integers
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1 # Simultaneous assignment

# 3. Prompt the student to answer "What is number1 - number2?"
answer = eval(input("What is "+ str(number1) + " x " +str(number2) + " ? "))

# 4. Check the answer and display the result
if number1 * number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", number1, 'x',number2, "is",
          number1 * number2, '.')
'''
# 4.12

