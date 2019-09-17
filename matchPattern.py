# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:57:48 2019

@author: AnkitaDatta
"""

#def count_substring(string, sub_string):
#    count= 0
#    for i in range(len(string)-len(sub_string)+1):
#        if string[i] == sub_string[0]:
#            flag = 1
#            for j in range(len(sub_string)):
#                if string[i+j] != sub_string[j]:
#                    flag = 0
#                    break
#            if flag == 1:
#                count += 1
#        
#    return count
#
#if __name__ == '__main__':
#    string = input().strip()
#    sub_string = input().strip()
#    
#    count = count_substring(string, sub_string)
#    print(count)
#    
    
    
    
#check string
if __name__ == '__main__':
     s = input()
    #
     print((s.isalnum()) )
     
     print (any(i.isalpha() for i in s))         
     print (any(i.isdigit() for i in s))   
     print (any(i.islower() for i in s))    
     print (any(i.isupper() for i in s))   
     