# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 08:29:17 2023

@author: Dell
"""
#Write python program to add all the items in the list 
def sum_list(sum_list):
    sum=0
    for x in sum_list:
        sum=sum+x
    return sum
print(sum_list([5,6,-8]))
#########################################
##Write python program to multiply all the items in the list 
def multiply_list(lst):
    tot = 1
    for x in lst:
        tot = tot*x
    return tot
print(multiply_list([1,2,-8]))
##########################################
#Write a Python program to get the largest number from a list. 
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))
#########################################
#Write a Python program to get the smallest number from a list. 
def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))
##############################################
'''
Write a Python program to count the number of strings which satisfies 
the condition that the string length is 2 or more and the first and last characters are the same.
from a given list of strings.given a list
['abc', 'xyz', 'aba', '1221']
'''
def match_words(words):
  ctr = 0
  for word in words:
    if len(word) > 2 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))  
##########################################
'''
Write a Python program to get a list, sorted in increasing 
order by the last element in each tuple from a given list 
of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

'''
def last(n): 
    return n[-1]

def sort_list_last(tuples):
    result=sorted(tuples, key=last)
    return result

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
################################################3
#Write a Python program to remove duplicates from a list.
#given the list a = [10,20,30,20,10,50,60,40,80,50,40]

lst1 = [10,20,30,20,10,50,60,40,80,50,40]
st1 = set(lst1)
#Since set removes duplicate items,hence list is converted to set
print(st1)
lst2=list(st1)
print(lst2)
#################################
#Write a Python program to clone or copy a list.
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)
##########################
#Write a Python program to find the list of words that are longer than
# n from a given list of words. 
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))
################################################
 #Write a Python function that takes two lists and returns 
 #True if they have at least one common member.
def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
##########################################
'''
Write a Python program to calculate the difference between the two lists. 
'''
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))
total_diff = diff1+diff2
print(total_diff)      
######################################
#Write a Python program to convert a list of characters into a string. 
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)
##############################
#Write a Python program to find the index of an item in a specified list.
num =[10, 30, 4, -6]
print(num.index(30))
#############################################3
#Write a Python program to append a list to the second list.
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list) 
###############################


