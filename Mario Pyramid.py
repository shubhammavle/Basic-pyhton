# -*- coding: utf-8 -*-
"""
Write a program to display mario pyramid

@author: Dell
"""

for i in range(4):
    for j in range(4):
        print("#",end="  ")
    print()
    
    for i in range(4):
        for j in range(i+1):
            print("#",end="  ")
        print()
        
        for i in range(4):
            for j in range(4-i):
                print("#",end="  ")
            print()