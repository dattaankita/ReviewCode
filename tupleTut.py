# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:41:27 2019

@author: AnkitaDatta
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t= tuple(integer_list)
    print(hash(t))
