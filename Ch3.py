#
'''
Chapter 3
Introduction to Programming Using Python
Create by Fei on Sep 14 2019
'''
'''
# 3.1
from math import sin, pi
radius1 = eval(input('Enter the length for the center to a vertex: '))
s1 = 2*radius1*sin(pi/5)
area1 = 1.5*3**0.5*s1**2
print('The area of the pentagon is',format(area1, '.2f'))

# 3.2
from math import *
x1, y1 = eval(input('Enter point 1(latitude and longitude) in degrees: '))
x2, y2 = eval(input('Enter point 2(latitude and longitude) in degrees: '))
x1 = radians(x1)
y1 = radians(y1)
x2 = radians(x2)
y2 = radians(y2)
radius2 = 6371.01
d = radius2*acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
print('The distance between the two points is', format(d,'.11f'),'km')

# 3.3
# combine 3.2 and Exercise 2.14

# 3.4
from math import pi, tan
side4 = eval(input('Enter the side: '))
area4 = 1.25*(side4**2)/tan(pi/5)
print('The area of the pentagon is', format(area4, '.14f'))

# 3.5
from math import tan, pi
n = eval(input('Enter the number of sides: '))
side5 = eval(input('Enter the side: '))
area5 = 0.25*n*side5**2/tan(pi/n)
print('The area of the polygon is', format(area5, '.14f'))

# 3.6
ch = eval(input('Enter an ASCII code: '))
print('The character is', chr(ch))
# 3.7
# clue: use the random with time.time

# 3.8
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
print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickels, "nickels\n",
      "\t", numberOfPennies, "pennies")
'''
# 3.9
name = input('Enter employee\'s name: ')
hours = eval(input('Enter number of hours worked in a week: '))
payrate = eval(input('Enter hourly pay rate: '))
fedtax = eval(input('Enter federal tax withholding rate: '))
statax = eval(input('Enter state tax withholding tate: '))
hourpay = hours*payrate
print('Employee Name:', name,
      '\nHours Worked:', hours,
      '\nPay Rate:',payrate,
      '\nGross Pay:', hourpay,
      '\nDeduction:\n'
      '\tFederal Withholding (',format(fedtax*100,'.1f'),'%):',hourpay*fedtax,
      '\n\tState Withholding (',format(statax*100,'.1f'),'%):',format(hourpay*statax,'.2f'),
      '\n\tTotal Deduction:', format(hourpay*(fedtax+statax),'.2f'),
      '\nNet Pay: ${0:.2f}'.format(hourpay*(1-fedtax-statax)))
'''
# 3.10
print('\u03b1 \u03b2 \u03b3 \u03b4 \u03b5 \u03b6 \u03b7 \u03b8')

# 3.11
num11 = reversed(input('Enter an integer: '))
print('The reversed number is ', end='')
for i in num11:
    print(i,end='')
print()
'''
