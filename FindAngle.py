# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:53:17 2019

@author: AnkitaDatta
"""

#import math 
#
#
#if __name__ == '__main__':
#    AB = int(input()) 
#    BC = int(input()) 
#    print(str(int(round(math.degrees(math.atan2(AB,BC)))))+'°')
#    
#    
    


#palindrome triangle    
#if __name__ == '__main__':
#    n = input()
#    for i in range(1,int(n)+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#         print(((10**i -1)//9)*((10**i -1)//9))

   
    
    
a= int(input())
b= int(input())


print(a//b)
print(a%b)
print(divmod(a,b))





import math


a= int(input())
b= int(input())
m= int(input())


print(pow(a,b))
print(pow(a,b,m))




for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i) //9) * i)
