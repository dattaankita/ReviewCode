## -*- coding: utf-8 -*-
#"""
#Created on Wed Aug 21 20:39:43 2019
#
#@author: AnkitaDatta
#"""
#
import numpy
# 
#def arrays(arr):
#    # complete this function
#    # use numpy.array
#    x= numpy.array(arr, float)
#    return numpy.flipud(x)
#
#arr = input().strip().split(' ')
#result = arrays(arr)
#print(result)
#
#
#lst= list(map(int, input().split()))
#my_array = numpy.array(lst)
#print(numpy.reshape(my_array,(3,3)))
#
#change_array = numpy.array([1,2,3,4,5,6])
#change_array.shape = (3, 2)
#print(change_array) 
#
#
#n,m = map(int, input().split())
#array = numpy.array([input().strip().split() for _ in range(n)], int)   
#print(numpy.transpose(array))
#print(numpy.ndarray.flatten(array))
#
#
#
#n,m,p= map(int, input().split())
#array_1 = np.array([input().split() for _ in range(n)], int)
#array_2 = np.array([input().split() for _ in range(m)], int)
#
#print(np.concatenate((array_1, array_2), axis = 0))   
#
#
#
#s= list(map(int, input().split()))
#print(numpy.zeros(s, dtype = numpy.int))
#print(numpy.ones(s, dtype = numpy.int))
#
#
#print numpy.identity(3)
#print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.
#print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
#
#
#n,m= map(int,input().split())
#numpy.set_printoptions(sign=' ')
#print (numpy.eye(n,m,k=0))



n, m= map(int, input().split())
array_A = numpy.array([input().split() for _ in range(n)], int)
array_B = numpy.array([input().split() for _ in range(n)], int)

print (numpy.add(array_A, array_B))
print (numpy.subtract(array_A, array_B)) 
print (numpy.multiply(array_A, array_B))    
print (numpy.floor_divide(array_A, array_B))    
print (numpy.mod(array_A, array_B))                             
print (numpy.power(array_A, array_B))



l= list(map(float,input().split()))
A = numpy.array(l, float)
numpy.set_printoptions(sign=' ')
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))



n, m= map(int, input().split())
my_array = numpy.array([input().split() for _ in range(n)], int)
X= numpy.sum(my_array, axis = 0)
print(numpy.prod(X, axis = 0)) 


n, m= map(int, input().split())
my_array= numpy.array([input().split() for _ in range(n)], int)
numpy.set_printoptions(sign=' ')
print(numpy.mean(my_array, axis = 1))
print (numpy.var(my_array, axis = 0))
print(numpy.around( numpy.std(my_array), 11))


import numpy as np 

n,m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)

b = np.array(b)

np.set_printoptions(legacy='1.13')
print(np.mean(b, axis = 1))
print(np.var(b, axis = 0))
print(np.std(b))





n, m= map(int, input().split())
array_A = numpy.array([input().split() for _ in range(n)], int)
array_B = numpy.min(array_A, axis = 1)
print(numpy.max(array_B, axis = 0))


n= int(input())
A = numpy.array([input().split() for _ in range(n)], int)
B = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(A, B))
#print(numpy.cross(A,B))  


A= list(map(int, input().split()))
B= list(map(int, input().split()))
A = numpy.array(A)
B = numpy.array(B)
print(numpy.inner(A,B))
print(numpy.outer(A,B))
 


y= list(map(float, input().split()))
x= int(input())
y= numpy.array(y)
print(numpy.polyval(y, x)) 
print numpy.poly([-1, 1, 1, 10]) 
print numpy.roots([1, 0, -1])
print numpy.polyint([1, 1, 1]) 
print numpy.polyder([1, 1, 1, 1])
print numpy.polyval([1, -2, 0, 2], 4)
print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)


print numpy.linalg.det([[1 , 2], [2, 1]])
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print numpy.linalg.inv([[1 , 2], [2, 1]]) 


n=int(input())
A = numpy.array([input().split() for _ in range(n)], float)
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(A))


n,m= map(int, input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
#The first is that each line has a set number of repetitions of '.|.', which are centered, and the rest is filled by '-'.
#The second is that the flag is symmetrical, so if you have the top, you have the bottom by reversing it. You only need to work on n // 2 (n is odd and you need the integer div because the remaining line is the "WELCOME" line).



def print_rangoli(n):
    # your code goes here
    import string
    alpha = string.ascii_lowercase

    #n = int(input())
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)