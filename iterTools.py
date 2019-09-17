# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:56:14 2019

@author: AnkitaDatta
"""

from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


#print(list(product([1,2,3],repeat = 2)))
#
#print(list(product([1,2,3],[3,4])))
#A = [[1,2,3],[3,4,5]]
#print(list(product(*A)))
### B = [[1,2,3],[3,4,5],[7,8]]



#cartesian product
#a = list(map(int,input().strip().split()))
#b = list(map(int,input().strip().split()))
 

#print(*product(a,b))

##arrangements
#nk = input().strip().split()
#s = nk[0]
#k = int(nk[1])
#print(*[''.join(i) for i in permutations(sorted(s),int(k))],sep='\n')
#

#
#nk = input().strip().split()
#s = nk[0].upper()
#k = int(nk[1])
#for i in range(1, k+1):
#    print(*[''.join(j) for j in combinations(sorted(s),i)],sep='\n')


#nk = input().strip().split()
#s = nk[0].upper()
#k = int(nk[1])
#print(*[''.join(i) for i in combinations_with_replacement(sorted(s),k)],sep='\n')
#

#from itertools import groupby
#print(*[(len(list(c)), int(k)) for k, c in groupby(input())])



#
#n = int(input())
#s = input().split()
#k = int(input())
#
#c = list(combinations(s,k))
#
#result = [1 for i in range(len(c)) if 'a' in c[i]]
#print(sum(result)/len(c))
#


#from itertools import product
#
#K,M = map(int,input().split())
#N = (list(map(int, input().split()))[1:] for _ in range(K))
#results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
#print(max(results))
#




# k,m = input().split()
# listoflists = []
# s = 0
# for i in range(int(k)):
#     sublist = []
#     sublist =input().split()
#     s = s + (int(max(sublist)) ** 2)
# print(s % int(m))


