# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:05:45 2023

@author: Dell
"""
#Write a Python program to create an iterator 
#from several iterables in a sequence and display 
#the type and elements of the new iterator.


from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)    
#List
result = chain_func([1,2,3], ['a','b','c','d'], [4,5,6,7,8,9])
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)

#Tuple
result = chain_func((10,20,30,40), ('A','B','C','D'), (40,50,60,70,80,90))
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)
    
#########################################
#Write a Python program that generates the running product 
#of elements in an iterable. 
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)

#List
result = running_product([1,2,3,4,5,6,7])
print("Running product of a list:")
for i in result:
    print(i)

#Tuple
result = running_product((1,2,3,4,5,6,7))
print("Running product of a Tuple:")
for i in result:
    print(i)
    
#################################################
#####################################
#Write a Python program to construct an infinite iterator that 
#returns evenly spaced values starting with a specified number and step. 
import itertools as it
start = 10
step = 1
print("The starting number is ", start, "and step is ",step)
my_counter = it.count(start, step)
# Following  loop will run for ever
print("The said function print never-ending items:")
for i in my_counter:    
    print(i)
########################################
#Write a Python program to generate an infinite cycle 
#of elements from an iterable.
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
# Following  loops will run for ever    
#List
result = cycle_data(['A','B','C','D'])
print("The said function print never-ending items:")
for i in result:
    print(i)

#String
result = cycle_data('Python itertools')
print("The said function print never-ending items:")
for i in result:
    print(i)
    
#############################
#Write a Python program to make an iterator that drops
# elements from the iterable as soon as an element is a positive number.
import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x : x < 0, nums)
nums = [-1,-2,-3,4,-10,2,0,5,12]
print("Original list: ",nums)
result = drop_while(nums)
print("Drops elements from the iterable when 
      a positive number arises \n",list(result))
#Alternate solution
def negative_num(x):
    return x < 0
def drop_while(nums):
    return it.dropwhile(negative_num, nums)
nums = [-1,-2,-3,4,-10,2,0,5,12]
print("Original list: ",nums)
result = drop_while(nums)
print("Drops elements from the iterable when a positive number arises \n",list(result)) 
######################################
#Write a Python program to create an iterator to get a 
#specified number of permutations of elements.
import itertools as it
def permutations_data(iter, length):
    return it.permutations(iter, length)
#List
result = permutations_data(['A','B','C','D'], 3)
print("\nIterator to get specified number of permutations of elements:")
for i in result:
    print(i)
###################################3
#Write a Python program to generate combinations 
#of a given length of a given iterable. 
import itertools as it
def combinations_data(iter, length):
    return it.combinations(iter, length)
#List
result = combinations_data(['A','B','C','D'], 2)
print("\nCombinations of an given iterable of length 2:")
for i in result:
    print(i)
#########################################
