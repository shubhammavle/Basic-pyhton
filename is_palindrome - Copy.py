# -*- coding: utf-8 -*-
"""
Write a program to find out the sentence is palindrome

@author: Dell
"""

def is_palindrome(input):
    if input=="":
        return "You entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
    return False   

print(is_palindrome("step on no pets"))
