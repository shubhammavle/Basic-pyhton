# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:08:01 2023

@author: Dell
"""

lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

####################
#we can write same method using list comprehension
lst=[num for num in range(0,20)]
print(lst)
#####################################
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)
##########################
#list comrehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
 
print(lst)
############################
lst=[f"{x}{y}"for x in range(3)for y in range(3) ]
print(lst)
##########################3
#set comrehension
set_one={ x  for x in range(3)   }
print(set_one)
#######################
#Dictionary comprehension
dict={x:x*x for x in range(3) }
print(dict)
##############################
#Generator
#It is another way of creating iterators
# in a simple way where 
#it uses the keyword “yield” 
#instead of returning it in a defined function.
# Generators are implemented using a function
gen=(x for x in range(3) )
print(gen)
for num in gen:
    print(num)
####################
gen=(x
     for x in range(3)
     
     )
next(gen)
##########################
gen=(x for x in range(3))     
next(gen)
next(gen)
#################################
#Function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
########################
#now instead of using for loop we can write our own generator
gen=range_even(6)
next(gen)
next(gen)
#################################
#Chaining Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'

passwords=["not-good","give'm-pass","00100=100"]

for password in  hide(lengths(passwords)):
    print(password)
######################################
#Enumerate
#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
##########
#same code can be implemented using enumerate
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
##############################
#Use of zip function
name=['dada','mama','kaka']
info=[9850,6032,9785] 
for nm,inf in zip(name,info):
    print(nm,inf)
##########################
#Use of zip function with mis match list
name=['dada','mama','kaka','baba']
info=[9850,6032,9785] 
for nm,inf in zip(name,info):
    print(nm,inf)    
 #It will not display excess mismatch item in name
# i.e.baba   
    
##############################
##zip_longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,3297]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
##########################################
#use of fill value instead None
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,3297]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
#########################################
#use of all(),if all the values are true then it will produce output
lst=[2,3,-6,8,9] #value must be non zero,+ve or -ve
if all(lst):
    print('all values are true')
else:
    print('Useless')
#########################
lst=[2,3,0,8,9]
if all(lst):
    print('all values are true')
else:
    print('Useless')


#################################
#use of any if any one non zero value
lst=[0,0,0,-8,0]
if any(lst):
    print('It has some value')
else:
    print('Useless')
##################
#use of any
lst=[0,0,0,0,0]
if any(lst):
    print('It has some value')
else:
    print('Useless')
###################
#count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
#################################
#Now let us start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
#############################
#cycle()
#suppose you have repeated tasks to be done,then you can use this method
import itertools

instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
    
###########################################
#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)
####################
#combinations()
from itertools import combinations
players=['John','Jani','Janardhan']
for i in combinations(players,2):
    print(i)
    
'''
('John', 'Jani')
('John', 'Janardhan')
('Jani', 'Janardhan')

'''
##################################
from itertools import permutations
players=['John','Jani','Janardhan']
for seat in permutations(players,2):
    print(seat)
"""
('John', 'Jani')
('John', 'Janardhan')
('Jani', 'John')
('Jani', 'Janardhan')
('Janardhan', 'John')
('Janardhan', 'Jani')
"""
################################
#product()
from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['virat','Manish','Sami']
for pair in product(team_a,team_b):
    print(pair)
"""
('Rohit', 'virat')
('Rohit', 'Manish')
('Rohit', 'Sami')
('Pandya', 'virat')
('Pandya', 'Manish')
('Pandya', 'Sami')
('Bumrah', 'virat')
('Bumrah', 'Manish')
('Bumrah', 'Sami')
"""
##################################
age=[27,17,21,19]
adults=filter( lambda age:age>=18,age) 
     
print([age for age in adults])
#########################
'''
In Python, assignment statements (obj_b = obj_a) do not create real copies.
It only creates a new variable with the same reference. 
So when you want to make actual copies of mutable objects (lists, dicts) 
and want to modify the copy without affecting the original, you have to be careful.
For 'real' copies we can use the copy module. 
However, for compound/nested objects (e.g. nested lists or dicts) 
and custom objects there is an important difference between shallow and deep copying: 
    - shallow copies: Only one level deep. It creates a new collection object 
    and populates it with references to the nested objects. 
    This means modyfing a nested object in the copy deeper than one level affects the original. 
    - deep copies: A full independent clone. It creates a new collection object 
    and then recursively populates it with copies of the nested objects found in the original.
'''
#Assignment operation
#This will only create a new variable with the same reference. Modifying one will affect the other.
list_a = [1, 2, 3, 4, 5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)

#[-10, 2, 3, 4, 5]
#[-10, 2, 3, 4, 5]
################################
#Shallow copy
#One level deep. Modifying on level 1 does not affect the other list. 
#Use copy.copy(), or object-specific copy functions/copy constructors.
import copy
list_a = [1, 2, 3, 4, 5]
list_b = copy.copy(list_a)

# not affects the other list
list_b[0] = -10
print(list_a)
print(list_b)
#[1, 2, 3, 4, 5]
#[-10, 2, 3, 4, 5]
########################################
#But with nested objects, modifying on level 2 or deeper does affect the other!
import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.copy(list_a)

# affects the other!
list_a[0][0]= -10
print(list_a)
print(list_b)
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#########################################
#Deep copies
#Full independent clones. Use copy.deepcopy().
import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)
# not affects the other
list_a[0][0]= -10
print(list_a)
print(list_b)
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

######################################################








#shallow copy and deep copy
#Copy an Object in Python
#Copy using = operator
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))
#2106866771712
print('New List:', new_list)
print('ID of New List:', id(new_list))
# same-2106866771712

#As you can see from the output both variables 
#old_list and new_list shares the same id i.e 2106866771712

#################################################
#Essentially, sometimes you may want to have 
#the original values unchanged and only modify 
#the new values or vice versa. 
#In Python, there are two ways to create copies:
    #
   # Shallow Copy
    #Deep Copy
#We use the copy module of Python for 
#shallow and deep copy operations. 
#Suppose, you need to copy the compound list say x.
x=[1,2,3]
import copy
copy.copy(x)
copy.deepcopy(x)
#Here, the copy() return a shallow copy of x. 
#Similarly, deepcopy() return a deep copy of x.
#A shallow copy creates a new object 
#which stores the reference of the original elements.
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
#This means it will create new and 
#independent object with same content. 
#To verify this, we print the both old_list and new_list.

#To confirm that new_list is different from old_list
# we try to add new nested object to original and check it.
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
#In the above program, 
#we created a shallow copy of old_list. 
#The new_list contains references to 
#original nested objects stored in old_list.
#Then we add the new list i.e [4, 4, 4] into old_list.
# This new sublist was not copied in new_list.

#However, when you change any nested objects 
#in old_list, the changes appear in new_list.
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)

#n the above program, we made changes to old_list 
#i.e old_list[1][1] = 'AA'. 
#Both sublists of old_list and new_list at index [1][1] 
#were modified. This is because, 
#both lists share the reference of same nested objects.

#Deep Copy

#A deep copy creates a new object and 
#recursively adds the copies of nested objects 
#present in the original elements.
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

#However, if you make changes to any nested objects
# in original object old_list, 
#you’ll see no changes to the copy new_list.
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
#In the above program, when we assign a new value to
# old_list, we can see only the old_list is modified.
# This means, both the old_list and the new_list are
# independent. 



import copy
lst1=[1,2,[3,4],5]
#using shallow copy
lst2=copy.copy(lst1)
print(f"The id of lst1 :{id(lst1)} and value is {lst1}and id of lst2:{id(lst2)} and the value is {lst2}")
"""
The id of lst1 :2335553487232 and value is [1, 2, [3, 4], 5]and id of lst2:2335553755904 and the value is [1, 2, [3, 4], 5]
"""
lst1=[1,2,[3,4],5]
#using shallow copy
lst3=copy.deepcopy(lst1)
print(f"The id of lst1 :{id(lst1)} and value is {lst1}and id of lst2:{id(lst3)} and the value is {lst3}")
"""
The id of lst1 :2335553487232 and value is [1, 2, [3, 4], 5]and id of lst2:2335552727424 and the value is [1, 2, [3, 4], 5]
"""
################################
# importing "copy" for copy operations
import copy
 
# initializing list 1
li1 = [1, 2, [3,5], 4]
 
# using deepcopy to deep copy
li2 = copy.deepcopy(li1)
 
# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 

 
# adding and element to new list
li2[2][0] = 7
 
# Change is reflected in l2
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print (li2[i],end=" ")
 

 
# Change is NOT reflected in original list
# as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")
########################################
#Shallow copying on the contraray any change made in copied object same 
#change is reflected in original object

# importing "copy" for copy operations
import copy
 
# initializing list 1
li1 = [1, 2, [3,5], 4]
 
# using copy to shallow copy
li2 = copy.copy(li1)
 
# original elements of list
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 

 
# adding and element to new list
li2[2][0] = 7
 
# checking if change is reflected
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
    print (li1[i],end="")
    ####################################
#unpacking of dictinary
friends={
    
    "Dale":9850,
    "male":6032
    
    }

contacts={
    
    "dada":8530,
    "mama":5286
    
    }
contacts.update(friends)
print(contacts)
####################################
######################################
#pipe operator
friends={"Satish":99021,
         "Ram":97603
         }
sham={"sham":85305}

all_friends=friends|sham
print(all_friends)
#############################
num=0
def change():
    num=1
change()
print(num)
#output will be 0
#In the same way we can not access outside of function 
#the value of variable declared
#inside the function
num=0
def change(x):
    x=1
change(x)
print(num)
#it will show an error

