# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:27:30 2019

@author: AnkitaDatta
"""

#import textwrap
#
#def wrap(string, max_width):
#
#    wrapper = textwrap.TextWrapper(width=max_width) 
#  
#    word_list = wrapper.wrap(text=string) 
#    
#    return "\n".join(word_list)
#
#if __name__ == '__main__':
#    string, max_width = input(), int(input())
#    result = wrap(string, max_width)
#    print(result)


def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        a = oct(i).lstrip("0o")
        if i > 9:
            b = hex(i).lstrip("0x").capitalize()
        else:
            b = hex(i).lstrip("0x")
        c = bin(i).lstrip("0b")
        print(i, a, b, c)
        #for i in range(1, n+1):
		#print('{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}'.format(i, w=len(bin(n))-2))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)