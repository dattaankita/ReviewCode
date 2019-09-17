# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:18:41 2019

@author: AnkitaDatta
"""

#Method 1 , My favourite
#array=list(map(int,input().split()))
#print(array)
##method 2
#inp=input().split()
#for i in inp:
#	array.append(int(i))
#print(array)
#a = int(input())
#
#
#n = (input().split())
#print(n[:a])
#
#arr = []
#for i in range(a):
#    x = int(input())
#    arr.append(x)
#    
#print(arr)
#arr = []
#for _ in range(n):
#    x = int(input())
#    arr.append(x)    


t= int(input())
for _ in range(t):
    n,d= input().split()   
    arr = []
    for _ in range(int(n)):
        x = int(input())
        arr.append(x)    
        
    for i in range(int(d)):    
        last = arr[int(n)-1];    
            
        for j in range(int(n)-1, -1, -1):    
            arr[j] = arr[j-1];    
                
        arr[0] = last;    
    print(arr)
    #Displays resulting array after rotation    
#    print("Array after right rotation: ");    
#    for i in range(0, len(arr)):    
#        print(arr[i])