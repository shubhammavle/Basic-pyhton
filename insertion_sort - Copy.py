# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:32:00 2022

@author: Dell
"""

lst=[2,6,5,1,3,4]

def insertion_sort(lst):
    for i in range(1,len(lst)):
        j=i
        while lst[j-1]>lst[j] and j>0:
            lst[j-1],lst[j]=lst[j],lst[j-1]
            j=j-1
            
print(insertion_sort(lst))
print(lst)
           