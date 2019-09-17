# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:21:34 2019

@author: AnkitaDatta
"""

#s= set()
#n = int(input())
#for i in range(n):
#    io= input()
#    s.add(io)
#    
#print(len(s))
#
##print(len(set([str(input()) for x in range(int(input()))])))
#
#n = int(input())
#s = set(map(int, input().split()))
#N = int(input())
#    
#for i in range(N):
#    st = input()
#    command = st.split()   
#    if command[0]=="remove":
#        s.remove(int(command[1]))
#    elif command[0]=="discard":
#        s.discard(int(command[1]))
#    elif command[0]=="pop":
#        s.pop()
#print(sum(s))
#
#
#m= int(input())
#a = set(map(int, input().split()))
#n= int(input())
#b = set(map(int, input().split()))
#s= a.union(b)
##s=a.intersection(b)
##s= a.diffrence(b)
##s= a.symmetric_difference(b)
#print(len(s))
#

#c = int(input())
#for _ in range(c):
#    d = int(input())
#    a= set(map(int, input().strip))
#    a = set()
#    for i in range(d):
#        x= int(input())
#        a.add(x)
#    e = int(input())
#    b = set()
#    for j in range(e):
#        y = int(input())
#        b.add(y)
#    print(a.issubset(b))
#    
#
#
#
#for _ in range(int(input())):
#    (_, a) = (int(input()),set(map(int, input().split())))
#    (_, b) = (int(input()),set(map(int, input().split())))
#    print(a.issubset(b))


#a = set(input().split())
#print(all(a > set(input().split()) for _ in range(int(input()))))

#for i in range(int(input())):
#    try:
#        a,b=map(int,input().split())
#        print(a//b)
#    except Exception as e:
#        print("Error Code:",e)
#        
        
import re


t = int(input())
for _ in range(t):
    s= input()
    try:
        re.compile(s)
        is_valid = True
    except re.error:
        is_valid = False

    print(is_valid)        


