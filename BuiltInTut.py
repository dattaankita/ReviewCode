# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:07:40 2019

@author: AnkitaDatta
"""

n, x = map(int, input().split()) 

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) ) 

for i in zip(*sheet): 
    print( sum(i)/len(i) )
    
    
x,k = map(int, input().split()) 
print(eval(input())==k)


eval(input())


N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))


nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
       
#map an lambda       
cube = lambda x: x ** 3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    lis = [0,1]
    for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])
    


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))       
       