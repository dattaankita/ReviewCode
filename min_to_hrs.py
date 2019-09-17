# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:25:23 2019

@author: AnkitaDatta
"""

import datetime
import time

def min_to_day(min):
        ctime = str(datetime.timedelta(minutes=min))
        c1time = time.strptime(ctime,"%d,%H,%M")
#        d = ctime.split(':')
#        d[0] = d[0].replace(',', '')
##        d.strftime("%d,%H,%M")
##        datetime.strptime(date_string, format) 
##        datetime(*(time.strptime(date_string, format)[0:6]))
#        d = ctime.split(':')
#        d[0] = d[0].replace(',', '')
#        s1 = float(d[2])
#        s2 = float(d[1])
#        if s1 >= 30:
#            s2+=1
#            s3= int(s2)
#            if s3 >= 60:
#                s4 = int(d[0])
#                s4+=1
#                print (str(s4) + " hr "+ str(s3) + " min" )
#            else:
#                print (d[0] + " hr "+ str(s3) + " min" )
#        else:
#            print (d[0] + " hr "+ d[1] + " min" )
        print(c1time)


min_to_day(1200)
min_to_day(1199.7)
min_to_day(29238.40)
