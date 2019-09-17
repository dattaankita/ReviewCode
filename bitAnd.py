# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:41:55 2019

@author: AnkitaDatta
"""


import array


if __name__ == '__main__':
#    t = int(input())
#
#    for t_itr in range(t):
#        nk = input().split()

    n = int(input())

    k = int(input())
    a = []
    
    for i in range(1,n+1):
        for j in range(k,n+1):
            x =i&j
            a.append(x)
            
    print(max(a))