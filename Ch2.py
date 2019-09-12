#
'''
Chapter 2
Introduction to Programming Using Python
Create by Fei on Sep 13 2019
'''
'''
# 2.1
Cel = eval(input('Enter a degree in Celsius: '))
Fah = (9/5)*Cel+32
print(Cel,'Celsius is',Fah,'Fahrenheit')

# 2.2
import math
rad, hei = eval(input('Enter the radius and length of a cylinder:'))
area = rad**2*math.pi
print('The area is',round(area*1e4)/1e4)
print('The volume is', round(area*hei*10)/10)

# 2.3
fe = eval(input('Enter a value for feet:'))
print(fe,'feet is',round(fe*0.305*1e4)/1e4,'meters')

# 2.4
po = eval(input('Enter a value in punds:'))
print(po,'pounds is',round(po*0.454*1e3)/1e3,'kilograms')

# 2.5
sub, rat = eval(input('Enter the subtotal and a gratuity rate:'))
print('The gratuity is',round(sub*rat)/100,\
      'and the total is',round(sub*(1+rat/100)*100)/100)

# 2.6
num6 = input('Enter a number between 0 and 1000: ')
sum6 = 0
for each in list(num6):
    sum6 += int(each)
print('The sum of the digits is', sum6)

# 2.7
min7 = eval(input('Enter the number of minutes: '))
print(min7,'minutes is approximatrly', int(min7/60/24/365),'years and',\
      int(min7/60/24)-int(min7/60/24/365)*365,'days')

# 2.8
wat = eval(input('Enter the amount of water in kilograms: '))
initem = eval(input('Enter the initial temperature: '))
fintem = eval(input('Enter the final temperature: '))
Qe = wat*(fintem-initem)*4184
print('The energy needed is', Qe)

# 2.9
faht = eval(input('Enter the temperature in Fahrenheit between -58 and 41: '))
vw = eval(input('Enter the wind speed in miles per hour: '))
wci = 35.74 + 0.6215*faht - 35.75*vw**0.16 + 0.4275*faht*vw**0.16
print('The wind chill index is',round(wci,5))

# 2.10
sp, ac = eval(input('Enter speed and acceleration: '))
length10 = sp*sp/ac/2
print('The minimum runway length for this airplane is', \
      round(length10,3),'meters')

# 2.11
finac = eval(input('Enter the final account valur: '))
yearat = eval(input('Enter the annual interest rate in percent: '))/1200
year = eval(input('Enter the number of years: '))*12
inidep = finac/((1+yearat)**year)
print('Initial deposit valur is',inidep)

# 2.12
print('a\tb\ta ** b')
for i in range(1,6):
    print(i,'\t',i+1,'\t',i**(i+1))

# 2.13
num13 = input('Enter the number: ')
for i in list(num13):
    print(i)

# 2.14
import math
x1, y1, x2, y2, x3, y3 = eval(input('Enter three points for a triangle: '))
side1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
side2 = math.sqrt((x1-x3)**2+(y1-y3)**2)
side3 = math.sqrt((x2-x3)**2+(y2-y3)**2)
s = 0.5*(side1+side2+side3)
area14 = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print('The area of the triangle is', round(area14,2))

# 2.15
side15 = eval(input('Enter the side: '))
area15 = 1.5 * (side15**2) * (3**(0.5))
print('The area of the hexagon is', round(area15, 4))

# 2.16
v0, v1, t = eval(input('Enter v0, v1 and t: '))
print('The average acceleration is', round((v1-v0)/t, 4))

# 2.17
weight17 = eval(input('Enter weight in pounds: '))*0.45359237
height17 = eval(input('Enter height in inches: '))*0.0254
print('BMI is', round(weight17/height17/height17,4))

# 2.18
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

# 2.19
inva = eval(input('Enter investment amount: '))
anrate = eval(input('Enter annual interest rate: '))/100/12
yea = eval(input('Enter number of years: '))*12
fuva = inva*(1+anrate)**yea
print('Accumulated value is', round(fuva, 2))

# 2.20
bal, intrate = eval(input('Enter balance and interest rate (e.g., 3 for 3%): '))
rate20 = round(bal*(intrate/1200), 4)
print('The interest is',rate20)

# 2.21
saveamount = eval(input('Enter the monthly saving amount: '))
totalamount = 0
for i in range(1, 7):
    totalamount = (saveamount+totalamount)*(1+0.00417)
totalamount = round(totalamount, 2)
print('After the sixth month, the account value is', totalamount)
'''
# 2.22
year2 = eval(input('Enter the number of years: '))
year22 = year2*3600*24*365
popu = 312032486 + year22//7 + year22//45 - year22//13
print('The population in', year2,'years is', popu)

