# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 09:56:22 2019

@author: AnkitaDatta
"""

#from collections import Counter
 
#myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
#print( Counter(myList))
#print(Counter(myList).items())
#print (Counter(myList).keys())
#print (Counter(myList).values())

#
##ShoeShop
#import collections
#
#numShoes = int(input())
#shoes = collections.Counter(map(int, input().split()))
#numCust = int(input())
#
#income = 0
#
#for i in range(numCust):
#    size, price = map(int, input().split())
#    if shoes[size]: 
#        income += price
#        shoes[size] -= 1
#
#print(income)


#
#from collections import defaultdict
#
#d = defaultdict(list)
#d['python'].append("awesome")
#d['something-else'].append("not relevant")
#d['python'].append("language")
#for i in d.items():
#    print(i)
#    
#
#
#
#n, m = map(int,input().split())
#d = defaultdict(list)
#list1 = []
#
#for i in range(n):
#    d[input()].append(i+1)
#
#for j in range(m):
#    list1 = list1 + [input()]
#    
#for k in list1: 
#    if k in d:
#        print (" ".join( map(str,d[k]) ))
#    else:
#        print(-1)





#from collections import namedtuple
#
#
#(n, categories) = (int(input()), input().split())
#Grade = namedtuple('Grade', categories)
#marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
#print((sum(marks) / len(marks)))



#from collections import OrderedDict
#
#ordinary_dictionary = {}
#ordinary_dictionary['a'] = 1
#ordinary_dictionary['b'] = 2
#ordinary_dictionary['c'] = 3
#print(ordinary_dictionary)
#
#ordered_dictionary = OrderedDict()
#ordinary_dictionary['a'] = 1
#ordinary_dictionary['b'] = 2
#ordinary_dictionary['c'] = 3
#print(ordinary_dictionary)
#
#
#
#from collections import OrderedDict
#d = OrderedDict()
#for _ in range(int(input())):
#    item, space, quantity = input().rpartition(' ')
#    d[item] = d.get(item, 0) + int(quantity)
#for item, quantity in d.items():
#    print(item, quantity)
#    
#    
    
#from collections import deque
#
#d = deque()
#d.append(1)
#print(d)
#d.appendleft(2)
#print(d)
#d.clear()
#print(d)
#d.extend('1')
#print(d)
#d.extendleft('234')
#print(d)
#d.count('1')
#d.pop()
#print(d)
#d.popleft()
#print(d)
#d.extend('7896')
#print(d)
#d.remove('2')
#print(d)
#d.reverse()
#print(d)
#d.rotate(3)
#print(d)
#
#
#
#
#from collections import deque
#
#
#n = int(input())
#d = deque()
#list = []
#for i in range(n):
#    list = input().strip().split()
#    if list[0] == "append":
#        d.append(list[1])
#    elif list[0] == "appendleft":
#        d.appendleft(list[1])
#    elif list[0] == "pop":
#        d.pop()
#    elif list[0] == "popleft":
#        d.popleft()
#
#print(*d)


