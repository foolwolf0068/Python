# -*- coding: utf-8 -*-
"""
Created on Sun Sep  15 20:49:06 2019
@author: foolwolf0068
"""
'''
# 5.1
cnt0, cnt1, cnt2, sum1 = 0, 0, 0,0
while True:
    num = eval(input('Enter an integer, the input ends if it is 0: '))
    cnt0 += 1
    if (num==0):
        break;
    if (num>0):
        cnt1 += 1
    else:
        cnt2 += 1
    sum1 += num
    aveg = sum1/(cnt0)
if(cnt0==1):
    print('You didn\'t enter any number')
else:
    print('The number of positives is', cnt1)
    print('The number of negatives is', cnt2)
    print('The total is', cnt0)
    print('The average is', aveg)

# 5.2
import random
import time

correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions
NUMBER_OF_QUESTIONS = 5 # Constant

startTime = time.time() # Get start time
while (count < NUMBER_OF_QUESTIONS):
    # Generate two random single-digit integers
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)
    # If number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1
    # Prompt the student to answer "What is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))
    # Grade the answer and display the result
    if number1 + number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong.\n", number1, "+", number2, "is", number1 - number2)
    count += 1
# Increase the count
endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correctCount, "out of",NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")

# 5.3
print('公斤\t|\t磅')
for i in range(1,200):
    print(i,'\t|\t',format(i*2.2,'.1f'))
'''
# 5.4
print('-'*30)
print('英里\t|\t  公里')
for i in range(1,11):
    print(i,'\t|\t',format(i*1.609,'.3f'))
    print('-'*30)
