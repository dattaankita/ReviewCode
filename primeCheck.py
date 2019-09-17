# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:43:50 2019

@author: AnkitaDatta
"""

import math


t=int(input())
for i in range(t):
    n=int(input())
    c=0
    sq = math.sqrt(n)
    for j in range(1,(int(sq) + 1)):
        if n % j == 0:  
            c += 1
    if c == 1:
        print("prime")
    else:
        print("Not prime")