## -*- coding: utf-8 -*-
#"""
#Created on Wed Mar 27 14:21:32 2019
#
#@author: AnkitaDatta
#"""
#
##regular expressions
#import re
#import urllib.request
#from re import findall
#
#
##Nameage= '''  Janica is 22 and Theon is 32
##Janica is 22 and Theon is 32
## '''
## 
##ages = re.findall(r'\d{1,3}', Nameage)
##names = re.findall(r'[A-Z][a-z]*', Nameage)
## 
##ageDict = {}
## 
##x=0
## 
##for i in names:
##    ageDict[i]= ages[x]
##    x+=1
##     
##print(ageDict)
#
#
#
##find word from string
##allinform = re.findall("inform","we need to inform about the information")
##for i in allinform:
##    print(i)
##    
#    
#    
#    
##find first and last index of string
#str = "we need to inform about the information"
#
#for i in re.finditer("inform",str):
#    loc = i.span()
#    print(loc)
#    
#
#
##find from string    
#str = "Sat, hat, mat, pat,"
#
#allstr = re.findall("[Shmp]at", str)    
#allstr = re.findall("[h-m]at", str)
#allstr = re.findall("[h-z]at", str)
#allstr = re.findall("[^h-m]at", str)
#for i in allstr:
#     print(i)    
##
#
##pattern substitute
#str = "Sat, hat, mat, pat"
#
#regex = re.compile("[m]at")
#food = regex.sub("food" , str)
#print(str)
#
#
##\\ problem
##randstr = "here is \\drogba"
##print(randstr)
##print(re.search(r"\\drogba", randstr))
#
#
##remove spaces
#randstr = '''
#keep the
# blue flag
# flying high
# '''
# 
# print(randstr)
# regex= re.compile("\n")
# randst= regex.sub(" ", randstr)
# print(randstr)
 
# #\b: backspace
# #\f:formfeed
# #\r:carriage return
# #\t,\v
# 
##number matching
#rand= "12345"
#print("Matches", len(re.findall("\d", rand)))
#
#print("Matches", len(re.findall("\d{5}", rand)))
#
#num= "123 1234 12345 123456 1234567"
#print("Matches", len(re.findall("\d{5,7}", num)))
#
#
##check phone number
##\w[a-zA-Z0-9]
##\w[^a-zA-Z0-9]
#phn= "412-563-6734"
#if re.search("\w{3}-\w{3}-\w{4}", phn):
#     print("it is a phone number")

#check names
#\s [\f\n\t\v]
#\S [\f\n\t\v]

#if re.search("\w{2,20}\s\w{2,20}","saurabh kulakshtra"):
#    print("fullname is vALID")
    
 
#email check
#email = "sk@aol.com md@.com @sed.com @df.com"
#print("email matches", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email)))
    


#webscraping
#url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"
#response = urllib.request.urlopen(url)
#html = response.read()
#htmlstr = html.decode()
#ndata = findall("\w{2,20}\s\w{2,20}", htmlstr)
#pdata = findall("\(\d{3}\) \d{3}-\d{4}",htmlstr)
#
#for i in ndata:
#    print(i)
#for i in pdata:
#    print(i)
    
    
    
    
#hackerrank
#regex_pattern = r"[.,]+"	# Do not delete 'r'.
#
#import re
#print("\n".join(re.split(regex_pattern, input())))


#search vowels between consonents
#import re
#
#VOWELS = 'aeiou'
#CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
#REGEX = '(?<=[' + CONSONANTS + '])([' + VOWELS + ']{2,})[' + CONSONANTS + ']'
#
#match = re.findall(REGEX, input(), re.IGNORECASE)
#if match:
#    print(*match, sep='\n')
#else:
#    print('-1')
#    
#    
#    
#re.findall(r'\w','http://www.hackerrank.com/')
#map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))

#start() and end()
#import re
#
#S = input()
#k = input()
#pattern = re.compile(k)
#r = pattern.search(S)
#
#if not r: 
#    print( "(-1, -1)")
#
#while r:
#    print("({0}, {1})".format(r.start(), r.end() - 1))
#    r = pattern.search(S,r.start() + 1)
#    
#
#m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
#m.group(0)
#m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
#m.groups()
#m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
#m.groupdict()

#import re
#m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
#print(m.group(1) if m else -1)
#
#
#import re
##
##for _ in range(int(input())):
##    print(bool(re.match(r'^[+-]?\d*\.\d*$', input())))
##    
##for _ in range(int(input())):
##	print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
#
#
#regex_pattern = r'^M{0,3}(CM){0,3}D?(CD){0,3}C{0,3}(XC){0,3}L?(XL){0,3}X{0,3}(IX){0,3}V?(IV){0,3}I{0,3}$|^m{0,3}(cm){0,3}d?(cd){0,3}c{0,3}(xc){0,3}l?(xl){0,3}x{0,3}(ix){0,3}v?(iv){0,3}i{0,3}$'	# Do not delete 'r'.
#print(str(bool(re.match(regex_pattern, input()))))
#
##check phone number
#N = int(input())
#for _ in range(N):
#    s= input()
#    m= re.match(r"[789]\d{9}$", s)
#    if m:
#        print("YES")
#    else:
#        print("NO")
#        
        
        
        
#import re
#import email.utils 
#
#
#n = int(input())
#for i in range(n):
#    t= email.utils.parseaddr(input())
#    m=re.match(r'[a-zA-Z][\w.-]*@[a-zA-Z]*\.[a-zA-Z]{0,3}$',t[1])
#    if m:
#        print(email.utils.formataddr(t))
#        
#        
#import re, sys
#[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]
        
        
#        
#from html.parser import HTMLParser1
#
#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):
#        print("Start :", tag)
#        for attr in attrs:
#            print ("->", attr[0],">",attr[1])
#
#    def handle_endtag(self, tag):
#        print ("End :", tag)
#
#    def handle_startendtag(self, tag, attrs):
#        print("Empty :", tag)
#
#n= int(input())
#for _ in range(n):
#    parser = MyHTMLParser()
#    parser.feed(input())
#    
#from html.parser import HTMLParser
#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):        
#        print ('Start :',tag)
#        for ele in attrs:
#            print ('->',ele[0],'>',ele[1])
#            
#    def handle_endtag(self, tag):
#        print ('End   :',tag)
#        
#    def handle_startendtag(self, tag, attrs):
#        print ('Empty :',tag)
#        for ele in attrs:
#            print ('->',ele[0],'>',ele[1])
#            
#MyParser = MyHTMLParser()
#MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))
#
#
#from html.parser import HTMLParser
#
#class MyHTMLParser(HTMLParser):
#    def handle_comment(self, data):
#        num=len(data.split('\n'))
#        if num > 1:
#            print('>>> Multi-line Comment')
#        else:
#            print('>>> Single-line Comment')
#        if data.strip():
#            print(data)
#        
#
#    def handle_data(self, data):
#        if data.strip():
#            print('>>> Data')
#            print(data)
#        # print("Data     :", data)
#  
# 
#html = ""    
## for i in range(n):
##     html_string += input().rstrip()+'\n'   
#for i in range(int(input())):
#    html += input().rstrip()
#    html += '\n'
#    
#parser = MyHTMLParser()
#parser.feed(html)
#parser.close()
#
#from html.parser import HTMLParser
#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):        
#        print (tag)
#        for ele in attrs:
#            print ('->',ele[0],'>',ele[1])
#            
#MyParser = MyHTMLParser()
#MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))
#
#
##unique empID
#import re
#
#for _ in range(int(input())):
#    uid= input()
#    uid = ''.join(sorted(uid))
#    # m =  re.match(r'[A-Z]{2,}\d{3,}\^[(.)\1]\^[a-zA-Z0-9]{10}$',uid)
#    a= bool(re.search(r'[A-Z]{2,}', uid))
#    b= bool(re.search(r'\d{3,}', uid))
#    c=(bool(re.search(r'^[a-zA-Z0-9]{10}$', uid)))
#    d=not bool(re.search(r'(.)\1', uid))
#    if a and b and c and d:
#        print("Valid")
#    else:
#        print("Invalid")
#
#
##XMLParser
#import sys
#import xml.etree.ElementTree as etree
#
#def get_attr_number(node):
#    # your code goes here
#    return sum(len(i.attrib) for i in node.iter())
#    
#
#if __name__ == '__main__':
#    sys.stdin.readline()
#    xml = sys.stdin.read()
#    tree = etree.ElementTree(etree.fromstring(xml))
#    root = tree.getroot()
#    print(get_attr_number(root))


#import xml.etree.ElementTree as etree
#
#maxdepth = 0
#def depth(elem, level):
#    global maxdepth
#    # your code goes here
#    if level == maxdepth:
#        maxdepth += 1
#
#    for i in elem:
#        depth(i, level + 1)
#
#if __name__ == '__main__':
#    n = int(input())
#    xml = ""
#    for i in range(n):
#        xml =  xml + input() + "\n"
#    tree = etree.ElementTree(etree.fromstring(xml))
#    depth(tree.getroot(), -1)
#    print(maxdepth)

#Decorators and Closures
#import re
#
#def wrapper(f):
#    def fun(l):
#        # complete the function
#        _numbers = []
#        for n in l:
#            s = re.match(r'^\+*[(91)0]*(\d{10})$', n).group()[-10:]
#            _numbers.append('+91 {0} {1}'.format(s[:5], s[5:]))
#        return f(_numbers)
#    return fun
#        
#    #return fun
##f(map(lambda x: "+91 " + x[-10:-5] + " " + x[-5:], l))
#
#@wrapper
#def sort_phone(l):
#    print(*sorted(l), sep='\n')
#
#if __name__ == '__main__':
#    l = [input() for _ in range(int(input()))]
#    sort_phone(l) 
#


import operator

#x.sort(key=itemgetter(1))
def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
        # x= sorted(people, key=operator.itemgetter(2))
        # return [f(p) for p in x]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')