# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:41:44 2019

@author: AnkitaDatta
"""

#if __name__ == '__main__':
#    x = int ( input()) 
#    y = int ( input()) 
#    z = int ( input())
#    n = int ( input()) 
#    ar = [] 
#    p = 0 
#    for i in range ( x + 1 ) : 
#        for j in range( y + 1): 
#            for k in range(z + 1):
#                if i+j+k != n: 
#                    ar.append([]) 
#                    ar[p] = [ i , j , k ] 
#                    p+=1
#        
#             
#    print(ar) 
#

#Captains room nunmber
k, arr= int(input()), list(map(int,input().split()))

set1 = set(arr)
print((sum(set1)*k - sum(arr))// (k-1))



