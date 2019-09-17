# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:03:05 2019

@author: AnkitaDatta
"""

#def swap_case(s):
#    #x= len(s)
#    a = ""
#    for i in s:
#        if i.isupper() == True:
#            a += (i.lower())
#        else:
#            a += (i.upper())
#    return a
#
#if __name__ == '__main__':
#    s = input()
#    result = swap_case(s)
#    print(result)
#
#

#     str = "THIS IS STRING EXAMPLE....WOW!!!" 
#     if str.isupper() == True:
#         print(str.lower())
#
#     str = "THIS is string example....wow!!!"
#     print(str.isupper())
    
    
#String Split and Join
#def split_and_join(line):
#    # write your code here
#    line1= line.split(" ")
#    line2 = "-".join(line1)
#    return line2
#
#if __name__ == '__main__':
#    line = input()
#    result = split_and_join(line)
#    print(result)
#    
    
#What's Your Name?
#def print_full_name(a, b):
#    print("Hello"+" "+a+" "+b+"! "+"You just delved into python.")
#
#if __name__ == '__main__':
#    first_name = input()
#    last_name = input()
#    print_full_name(first_name, last_name)
#    
    
#Mutations
def mutate_string(string, position, character):
    st =  string[:position] + character + string[position+1:]
    return st

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)