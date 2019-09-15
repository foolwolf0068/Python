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

# 4.11
dayOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
nameOfMonth = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month, year = eval(input('Enter the month and year: '))
isLeapYear = (year%400==0)or((year%4==0)and(year%100!=0))
print(nameOfMonth[month-1],year,'has',end=' ')
if((month==2) and isLeapYear):
    print('29 days.')
else:
    print(dayOfMonth[month-1],'days.')

# 4.12
num12 = eval(input('Enter an integer: '))
print('Is',num12,'divisible by 5 and 6?',(num12%30==0))
print('Is',num12,'divisible by 5 or 6?',(num12%5==0 or num12%6==0))
print('Is',num12,'divisible by 5 or 6, but not both?',
      (num12%5==0 or num12%6==0)and(num12%30!=0))

# 4.13
import sys

# Prompt the user to enter filing status
status = eval(input(
"(0-single filer, 1-married jointly,\n" +
"2-married separately, 3-head of household)\n" +
"Enter the filing status: "))

# Prompt the user to enter taxable income
income = eval(input("Enter the taxable income: "))

# Compute tax
tax = 0

if status == 0: # Compute tax for single filers
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
             (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
        (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
        (372950 - 171550) * 0.33 + (income - 372950) * 0.35
elif status == 1: # Compute tax for married file jointly
    #print("Left as exercise")
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10 + (income - 16701) * 0.15
    elif income <= 137050:
        tax = 16700 * 0.10 + (67900 - 16701) * 0.15 + \
             (income - 67900) * 0.25
    elif income <= 208850:
        tax = 16700 * 0.10 + (67900 - 16701) * 0.15 + \
             (137050 - 67901) * 0.25 + (income - 137051) * 0.28
    elif income <= 372905:
        tax = 16700 * 0.10 + (67900 - 16701) * 0.15 + \
             (137050 - 67901) * 0.25 + (208850 - 137051) * 0.28 \
             (income - 208851) * 0.33
    else:
        tax = 16700 * 0.10 + (67900 - 16701) * 0.15 + \
             (137050 - 67901) * 0.25 + (208850 - 137051) * 0.28 \
             (372950 - 208851) * 0.33 + (income - 372951) * 0.35
elif status == 2: # Compute tax for married separately
    #print("Left as exercise")
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 835 + (income - 8351) * 0.15
    elif income <= 68525:
        tax = 835 + (33950 - 8351) * 0.15 + (income - 33951) * 0.25
    elif income <= 104425:
        tax = 835 + (33950 - 8351) * 0.15 + (68525- 33951) * 0.25 + \
              (income - 68526) * 0.28
    elif income <= 186475:
        tax = 835 + (33950 - 8351) * 0.15 + (68525- 33951) * 0.25 + \
              (104425 - 68526) * 0.28 + (income - 104426) * 0.33
    else:
        tax = 835 + (33950 - 8351) * 0.15 + (68525- 33951) * 0.25 + \
              (104425 - 68526) * 0.28 + (186475 - 104426) * 0.33 +\
              (income - 186476) * 0.35
elif status == 3: # Compute tax for head of household
    #print("Left as exercise")
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 1195 + (income - 11951) * 0.15
    elif income <= 117450:
        tax = 1195 + (45500 - 11951) * 0.15 + (income - 45501) * 0.25
    elif income <= 190200:
        tax = 1195 + (45500 - 11951) * 0.15 + (117450 - 45501) * 0.25 + \
              (income - 177451) * 0.28
    elif income <= 372950:
        tax = 1195 + (45500 - 11951) * 0.15 + (117450 - 45501) * 0.25 + \
              (190200 - 177451) * 0.28 + (income - 190201) * 0.33
    else:
        tax = 195 + (45500 - 11951) * 0.15 + (117450 - 45501) * 0.25 + \
              (190200 - 177451) * 0.28 + (372950 - 190201) * 0.33+ \
              (income - 372951) * 0.35
else:
    print("Error: invalid status")
    sys.exit()

# Display the result
print("Tax is", format(tax, ".2f"))

# 4.14
from random import randint
answer = randint(0,1)
guess = eval(input('0-Head, 1-Tail, Enter the integer: '))
if(answer==0):
    print('The flipped coin displays the head.')
    if(answer==guess):
        print('You are right.')
    else:
        print('You are wrong.')
else:
    print('The flipped coin displays the tail.')
    if(answer==guess):
        print('You are right.')
    else:
        print('You are wrong.')

# 4.15
import random

# Generate a lottery number
lottery = random.randint(100, 1000)
# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (two digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

# Get digits from guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if(guess==lottery):
    print("Exact match: you win $10,000")
elif(guessDigit2==lotteryDigit1 and \
     guessDigit1==lotteryDigit2):
    print("Match all digits: you win $3,000")
elif(guessDigit1 == lotteryDigit1
    or guessDigit1 == lotteryDigit2
    or guessDigit2 == lotteryDigit1
    or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")

# 4.16
from random import randint
ch = randint(ord('A'),ord('Z')+1)
print('The random upper charactor is', chr(ch))

# 4.17
from random import randint
answer17 = randint(0,2)
name = ['scissor','rock','paper']
guess17 = eval(input('scissor (0), rock (1), paper (2): '))
if(answer17==guess17):
    print('The computer is',name[answer17],'. You are',name[answer17],
          'too. It is a draw.')
else:
    print('The computer is',name[answer17],'. You are',name[guess17],'. You',end=' ')
    if(answer17==0):
        if(guess17==1):
            print('win.')
        else:
            print('lose.')
    elif(answer17==1):
        if(guess17==2):
            print('win.')
        else:
            print('lose.')
    else:
        if(guess17==0):
            print('win.')
        else:
            print('lose.')

# 4.18
exchangeRate = eval(input('Enter the exchange rate from dollars to RMB: '))
verse = eval(input('Enter 0 to convert dollars to RMB and 1 vice versa: '))
if(verse==0):
    amount = eval(input('Enter the dollars amount: '))
    print('$',amount,'is {0:.2f}'.format(amount*exchangeRate),'yuan')
elif(verse==1):
    amount = eval(input('Enter the RMB amount: '))
    print('￥',amount,'is $ {0:.2f}'.format(amount/exchangeRate))
else:
    print('Incorrect input')

# 4.19
s1, s2, s3 = eval(input('Enter three edges: '))
if(s1<=0 or s2<=0 or s3<=0):
    print('The input is invalid.')
else:
    if(s1+s2>s3 and s1+s3>s2 and s2+s3>s1):
        print('The perimeter is', s1+s2+s3)
    else:
        print('The input is invalid.')

# 4.20
faht = eval(input('Enter the temperature in Fahrenheit between -58 and 41: '))
vw = eval(input('Enter the wind speed in miles per hour: '))
if((-58<=faht<=41) and (vw>=2)):
    wci = 35.74 + 0.6215*faht - 35.75*vw**0.16 + 0.4275*faht*vw**0.16
    print('The wind chill index is',round(wci,5))
else:
    print('The input is in valid')

# 4.21
from math import floor
year = eval(input('Enter year: (e.g., 2008): '))
m = eval(input('Enter month: 1-12: '))
q = eval(input('Enter the day of the month: 1-31: '))
week = ['Saturday','Sunday','Monday','Tursday','Wednsday','Thursday','Friday']
if(year>0 and 1<=m<=12 and 1<=q<=31):
    if(m==1 or m==2):
        m += 12
    k = year%100
    h = (q+floor(26*(m+1)/10)+k+floor(k/4)+floor(floor(year/100)/4) +5*floor(year/100))%7
    print('Day of the week is',week[h])
else:
    print('The input is invalid')

# 4.22
x, y = eval(input('Enter a point with two coordinates: '))
print('Point ({0:.1f}, {1:.1f}) is'.format(x,y),end=' ')
if(x*x+y*y <= 100):
    print('in the circle')
else:
    print('not in the circle')

# 4.23
x, y = eval(input('Enter a point with two coordinates: '))
print('Point ({0:.1f}, {1:.1f}) is'.format(x,y),end=' ')
if(-5<=x<=5 and -2.5<=y<=2.5):
    print('in the rectangle')
else:
    print('not in the rectangle')
    
# 4.24
from random import randint
size = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
color = ['Club','Heart','Diamond','Spade']
numOfSize = randint(0,12)
numOfColor = randint(0,3)
print('The card you picked is the',size[numOfSize],'of',color[numOfColor])

# 4.25
x1, y1, x2, y2, x3, y3, x4, y4 = eval(input('Enter x1, y1, x2, y2, x3, y3, x4, y4: '))
a, b = y1-y2,x2-x1
e = a*x1 + b*y1
c, d = y3-y4, x4-x3
f = c*x3 + d*y3
div = a*d - b*c
if(div != 0):
    x = (e*d - b*f)/div
    y = (a*f - e*c)/div
    print('The intersecting point is at({0:.5f}, {1:.5f})'.format(x, y))
else:
    print('The two lines are parallel')

# 4.26
num26 = input('Enter a three-digit integer: ')
if((99<eval(num26)<1000) and num26[0]==num26[-1]):
    print(eval(num26),'is a palindrome')
else:
    print(eval(num26),'is not a palindrome')

# 4.27
x, y = eval(input('Enter a point\'s x- and y-coordinates: '))
if((0<=x<=200)):
    y1 = -0.5*x + 100
    if( y1>y):
        print('The point is in the triangle')
    else:
        print('The point is not in the triangle')
else:
    print('The point is not in the triangle')

# 4.28
cx1, cy1, width1, height1 = eval(input('Enter r1\'s center x-, y-coordinates, width, and heiht: '))
cx2, cy2, width2, height2 = eval(input('Enter r2\'s center x-, y-coordinates, width, and heiht: '))
if (width2*height2 > width1*height1):
    cx1, cx2 = cx2, cx1
    cy1, cy2 = cy2, cy1
    width1, width2 = width2, width1
    height1, height2 = height2, height1
x11, x12 = cx1-width1/2, cx1+width1/2
y11, y12 = cy1-height1/2, cy1+height1/2
x21, x22 = cx2-width2/2, cx2+width2/2
y21, y22 = cy2-height2/2, cy2+height2/2

if(x11<=x21 and x22<=x12 and y11<=y21 and y22<=y12):
    print('r2 is inside r1')
elif(x21>x12 or x22<x11 or y11>y22 or y12<y21):
    print('r2 does not overlap r1')    
else:
    print('r2 overlaps r1')

# 4.29
from math import sqrt
cx1, cy1, radius1 = eval(input('Enter circle1\'s center x-, y-coordinates, and radius: '))
cx2, cy2, radius2 = eval(input('Enter circle2\'s center x-, y-coordinates, and radius: '))
if(radius1<radius2):
    cx1,cx2 = cx2, cx1
    cy1,cy2 = cy2, cy1
    radius1, radius2 = radius2, radius1
d = sqrt((cx1-cx2)**2 + (cy1-cy2)**2)
if(d>radius1+radius2):
    print('Circle2 does not overlap circle1')
elif (d<=radius1):
    print('Circle2 is inside circle1')
else:
    print('Circle2 overlaps circle1')

# 4.30
from time import gmtime, strftime
tzone0 = input("Enter the time zone offset to GMT: ")
if (-10<int(tzone0)<0):
    tzone = tzone0[0]+'0'+tzone0[-1]
elif (0<=int(tzone0)<10):
    tzone = '+0'+tzone0
elif (10<=int(tzone0)):
    tzone = '+'+tzone0
timeformat = "%H:%M:%S" +tzone+"00"
time18 = strftime(timeformat, gmtime())
print('The current time is '+time18[1:-5])

# 4.31
x1, y1, x2, y2, x3, y3 = eval(input('Enter coordinates for the three points p0, p1 and p2: \n'))
d = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
if(d>0):
    print('p2 is on the left side of the line from p0 to p1')
elif(d==0):
    print('p2 is on the same line from p0 to p1')
else:
    print('P2 is on the right side of the line from p0 to p1')

# 4.32
x1, y1, x2, y2, x3, y3 = eval(input('Enter coordinates for the three points p0, p1 and p2: \n'))
d = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)

if(d==0 and x1<=x3<=x2):
    print('p2({0:.1f},{1:.1f}) is on the line segment from p0({2:.1f},{3:.1f}) to p1({4:.1f},{5:.1f})'.format(x3, y3, x1, y1, x2, y2))
else:
    print('p2({0:.1f},{1:.1f}) is not on the line segment from p0({2:.1f},{3:.1f}) to p1({4:.1f},{5:.1f})'.format(x3, y3, x1, y1, x2, y2))

# 4.33
nameOfHex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
num33 = eval(input('Enter a decimal value (0 to 15): '))
if(0<=num33<=15):
    print('The hex value is',nameOfHex[num33])
else:
    print('Invalid input')
'''
# 4.34
nameOfHex = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
             'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
num34 = input('Enter a hex character: ')
if(num34 in nameOfHex):
    print('The decimal value is',nameOfHex[num34])
elif(num34 in ['a','b','c','d','e','f']):
    print('The decimal value is',nameOfHex[num34.upper()])
else:
    print('Invalid input')
