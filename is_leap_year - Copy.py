# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:05:10 2022

@author: Dell
"""

def is_leap_year(year):
    if((year>0) and (year%4==0) and (year%100==0) and (year%400==0)):
      return True
    return False

#is_leap_year=lambda year:[if((year>0) and (year%4==0) and (year%100==0) and (year%400==0)) return True else False]

print(is_leap_year(2000))


