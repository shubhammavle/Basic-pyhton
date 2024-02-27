# -*- coding: utf-8 -*-
"""
Write a program to find out is duplicate elements from list

@author: Dell
"""

lst1=[1,2,3,5,5,6,7]

def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        # compare current number with next number
        if(lst1[i]==lst1[i+1]):
            return True
    return False    

print(is_duplicate(lst1))
