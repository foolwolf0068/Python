#
'''

Create by Fei on Sep 13 2019
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
