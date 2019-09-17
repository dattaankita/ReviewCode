# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:58:43 2019

@author: AnkitaDatta
"""

#def average(array):
#    # your code goes here
#    set1 = set(array) 
#    avg = sum(set1)/len(set1)
#    return avg
#
#if __name__ == '__main__':
#    n = int(input())
#    arr = list(map(int, input().split()))
#    result = average(arr)
#    print(result)
#    
#    
#    
##get int values
#newlis = list(map(int, lis))
##create set
#myset = {1, 2} # Directly assigning values to a set
#myset = set()  # Initializing a set
#myset = set(['a', 'b'])
#
#a,b = [set(input().split()) for _ in range(4)][1::2]
#print ('\n'.join(sorted(a^b, key=int)))



#if __name__ == '__main__':
#    (_, A) = (int(input()),set(map(int, input().split())))
#    B = int(input())
#    for _ in range(B):
#        (command, newSet) = (input().split()[0],set(map(int, input().split())))
#        getattr(A, command)(newSet)
#
#    print (sum(A))
#    
#    
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, no):
        return Points(self.x-no.x, self.y-no.y, self.z-no.z)

    def dot(self, no):
        return self.x*no.x + self.y*no.y + self.z*no.z

    def cross(self, no):
        return Points(self.y*no.z-self.z*no.y, self.z*no.x-self.x*no.z, self.x*no.y-self.y*no.x)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
    def __add__(self, other):
        return Points(self.x+other.x, self.y+other.y, self.z+other.z)



if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))