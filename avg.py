# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:09:48 2019

@author: AnkitaDatta
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = student_marks[query_name]
    l= len(query_marks)
    s=0
    for i in range(l):
       s = s + query_marks[i]
                
    a=float(s)/l
    print("%.02f" % a)
            