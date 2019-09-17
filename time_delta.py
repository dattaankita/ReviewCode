# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:14:43 2019

@author: AnkitaDatta
"""

##!/bin/python3
#
#import math
#import os
#import random
#import re
#import sys
#from datetime import datetime as dt
#
## Complete the time_delta function below.
#def time_delta(t1, t2):
#    fmt = '%a %d %b %Y %H:%M:%S %z'
#    tx1 = dt.strptime(t1, fmt)
#    tx2 = dt.strptime(t2, fmt)
#    x = int(abs(tx1 - tx2).total_seconds())
#    return str(x)
#
#
#     
#
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    t = int(input())
#
#    for t_itr in range(t):
#        t1 = input()
#
#        t2 = input()
#
#        delta = time_delta(t1, t2)
#        
#        fptr.write(delta + '\n')
#
#    fptr.close()
#
#
##import datetime
##a = datetime.datetime.now()
##b = datetime.datetime.now()
##print(a - b)



import calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

#find the day
import datetime 
import calendar 
  

if __name__ == '__main__':
    date = input()
    d2 = datetime.datetime.strptime(date, '%m %d %Y').weekday() 
    d3 = calendar.day_name[d2].upper()
    print (d3) 
