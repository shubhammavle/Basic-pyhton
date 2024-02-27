# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:06:19 2022

@author: Dell
"""

num= [5, 3, 8, 6, 7, 2]

def sort(num):
       for i in range(len(num)-1,0,-1):
           for j in range(i):
               if num[j]>num[j+1]:
                   temp=num[j]
                   num[j]=num[j+1]
                   num[j+1]=temp
       return num
print(sort(num))         

