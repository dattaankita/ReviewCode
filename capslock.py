# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:58:10 2019

@author: AnkitaDatta
"""

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys
#
## Complete the solve function below.
##s = "chris gayle"
#def solve(s):
#    s = "chris gayle"
#    x= s.split(" ")
#
#    for i in range(len(x)):
#        x[i] = x[i].capitalize()
#    str1 = ' '.join(str(e) for e in x)
#    print(str1)
#    return str1
#
#
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    s = input()
#
#    result = solve(s)
#
#    fptr.write(result + '\n')
#
#    fptr.close()


#s = "chris gayle"
#x= s.split(" ")
#for i in range(len(x)):
#    x[i] = x[i].capitalize()
#str1 = ' '.join(str(e) for e in x)
#print(str1)



# import math


# z= complex(input())

# x = z.real
# y = z.imag
# print(math.sqrt(x ** 2 + y ** 2))
# print(math.atan(y/x))
import cmath

r = complex(input().strip())

print(cmath.polar(r)[0])
print(cmath.polar(r)[1])