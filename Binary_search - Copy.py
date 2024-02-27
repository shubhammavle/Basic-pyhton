# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:27:24 2022

@author: Dell
"""

lst=[4,7,8,12,45,99]
pos=-1
def search(lst,n):
    l=0
    u=len(lst)-1
    while l<u:
        mid=(l+u)//2
        if lst[mid]==n:
            globals()['pos']=mid
            
            return "The searched value is at  "+str(pos)
        else:
            if lst[mid]<n:
                l=mid
            else:
                u=mid
                
print(search(lst,7))
    