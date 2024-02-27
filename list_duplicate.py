# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:28:20 2022

@author: Dell
"""

lst1=[1,2,3,7,6,3,7,8,6]
def list_duplicate(lst1):
    lst2=[]
    for x in range(len(lst1)):
        for j in range((x+1),len(lst1)):
            if lst1[x]==lst1[j] and lst1[x] not in lst2:
                lst2.append(lst1[x])
    return lst2

print(list_duplicate(lst1))
     