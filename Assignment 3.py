#Task 1
a= int(input("Enter a Number: "))

def fact(x):
    if x<2:
        return 1
    else:
        return (x*(fact(x-1)))

facto = fact(a)
print('Factorial of ',a,' is:',facto)

# Task 2
import math
from math import *

Val = int(input("Enter a number: "))
def calcu(b):
    sqare = math.sqrt(Val)
    loge = math.log(Val,e)
    sine = math.sin(Val)
    print("Square root : ",sqare)
    print("Logarithm : ",loge)
    print("Sine : ",sine)

calcu(Val)