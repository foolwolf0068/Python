# -*- coding: utf-8 -*-
"""
Created on Wed Sep  11 20:49:06 2019
@author: foolwolf0068
"""
# 1.1
print("Welcome to Python")
print("Welcome to Computer Science")
print("Programming is fun")

# 1.2
print('Welcome to Python\n'*5);

# 1.3
a, b, c, s = 'F','U','N', ' '
print(a*7+s*3+b+s*5+b+s*3+c*2+s*5+c*2)
print(a*2+s*8+b+s*5+b+s*3+c*3+s*4+c*2)
print(a*7+s*3+b+s*5+b+s*3+c*2+s+c+s*3+c*2)
print(a*2+s*9+b+s*3+b+s*4+c*2+s*2+c+s*2+c*2)
print(a*2+s*10+b*3+s*5+c*2+s*4+c*3)

# 1.4
print("a\ta^2\ta^3")
for i in range(1,5):
    print(str(i)+'\t'+str(i**2)+'\t'+str(i**3))

# 1.5
print((9.5*4.5-(2.5*3))/(45.5-3.5))

# 1.6
sum5 = str(sum(list(range(1,10))))
print('1+2+3+4+5+6+7+8+9 = '+sum5)

# 1.7
pai = 4*(1-1/3+1/5-1/7+1/9-1/11)
print(pai)
print(pai+4/13-4/15)

# 1.8
import math
radius = 5.5;
area = radius**2*math.pi
perimeter = 2*radius*math.pi
print('area = ',area,'\tperimeter = ',perimeter)

# 1.9
width = 4.5
height = 7.9
print('area = ',width*height)

# 1.10
print('Speed=',14/1.6/(45/60+30/3600))

# 1.11
yeartime = 365*24*3600
p = 3120324986
for i in range(1,6):
    print('第',i,'年人口是：',end = '')
    p += (yeartime//7-yeartime//13+yeartime//45)
    print(p,'\n')
