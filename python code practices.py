# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:07:07 2022

@author: Dell
"""

import pandas as pd
df=pd.DataFrame({'vehicle':['Maruti 800','Santro','Pulsor','Shine'],'Type':['car','car','bike','bike']})
print(df)
df.groupby('Type').count()
#####################
df=pd.DataFrame()
cars=["maruti","Honda","TATA"]
bikes=["Honda","TVS","Bajaj"]
df["cars"]=cars
df["bikes"]=bikes
df
##################################################
df=pd.DataFrame()
cars=["Maruti","Tata","Mahindra"]
bikes=["Honda","Bajaj","TVS"]
d={"cars":cars,"Bikes":bikes}
df=pd.DataFrame(d)
df
######################################
EName=['Ram','Sham','Gansham']
Job=['Clerk','Accountant','Manager']
Emp_no=['212','321','456']
Hire_date=['22-05-21','12-03-12','23-8-20']
Loc=['Jaipur','Pune','Mumbai']
Dept_no=['10','20','30']
df1=pd.DataFrame()
Employee={"EName":EName,"Job":Job,"Emp_no":Emp_no,"Hire_date":Hire_date,"Loc":Loc,"Dept_no":Dept_no}
df1=pd.DataFrame(Employee)
df1
##############################
Dept_no=['10','20','30']
Dept_name=["office","Account","Production"]
Loc=['Jaipur','Pune','Mumbai']
df2=pd.DataFrame()
Dept={"Dept_no":Dept_no,"Dept_name":Dept_name,"Loc":Loc}
df2=pd.DataFrame(Dept)
df2
############################
emp_dept=pd.merge(df1,df2,on=["Dept_no"],how='inner')
emp_dept
###################
emp_dept_left=pd.merge(df1,df2,on=["Dept_no"],how='left')
emp_dept_left
################################
emp_dept_rt=pd.merge(df1,df2,on=["Dept_no"],how='right')
emp_dept_rt
#############################
#How to access data from dataframe using value index
a=[1,2,3]
df1.index=a
df1
df1.loc[2]
#################################
#How will you find central tendancy of an array
import numpy as np
n1=np.array([10,20,30,40,50,60])
print(np.mean(n1))
print(np.median(n1))
print(np.std(n1))
###############################
lst=[13,17,98,54,32]
def search(lst,value):
      for i in range(len(lst)):
          if (lst[i]==value):
              return "Value has been found at location of {}".format(i)
      return "value is not found"

print(search(lst,35))
#####################################

def vovels(input):
    if input==" ":
        return " you have entered wrong input"
    else:
        count=0
        str=input.lower()
        for i in range(len(str)):
            
            if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' ):
              count=count+1
        return count

print(vovels('aeiou'))
##################################
lst=[1,2,5,6,8,10,15,21]
def return_sum(lst):
    sum=0
    for i in range(len(lst)):
        if lst[i]%5==0 or lst[i]%7==0:
           sum=sum+lst[i]
    return sum 

print(return_sum(lst))
#######################
lst=[1,2,4,6,7,9,9,10]

def is_duplicate(lst):
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            return "The duplicate number is found at position {}".format(i)
    return " no duplicate number"
    
print(is_duplicate(lst))  
##################################
lst=[1,2,3,4,5,5,7,9,9]
def list_duplicate(lst):
    lst2=[]
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            lst2.append(lst[i])
    return lst2

print(list_duplicate(lst))
##############################
def leap_year(input):
    if((input>0) and (input%4==0) and (input%100==0) and (input%400==0)): 
         return True
    return False

print(leap_year(1900))
###########################################
def reverse_string(input):
    if input==" ":
        return "The wrong input has been entered"
    else:
        str=input[::-1]
    return str
print(reverse_string('This'))    
##################################
def reveresed_words(input):
    if input==" ":
       return "You have enterd wrong input"
    else:
         words=input.split()
         reverse=" ".join(reversed(words))
    return reverse   

print(reveresed_words("this is reverse"))      
############################333
def is_palindrome(input):
    if input==" ":
       return " Wrong input entered"
    else:
         str=input[::-1]
         if str==input:
            return True
    return False         

print(is_palindrome("allaw"))
####################################

def is_anagram(input1,input2):
    if input1==" " or input2==" ":
        return " The wrong input"
    else:
        str1=input1.lower()
        str2=input2.lower()
        if(len(str1) != len(str2)):
            return False
    return True

print(is_anagram("elboweq","below"))
####################################
def febbo(n):
    lst=[]
    previous=0
    current=1
    lst.append(current)
    for i in range(2,n-1):
        previous,current=current,previous+current
        lst.append(current)
    return lst

print(febbo(8))
################################
def mario(n1,n2):
    for i in range(n1):
        for j in range(4-i):
            print("#",end="")
        print()
    
   
        
print(mario(4,4))  
##############################
def prime_num(num):
    for i in range(2,num):
        if (num%i==0):
            return "The number is not prime"
    return "The number is prime"

print(prime_num(13))    
#####################
numbers=[1,4,6]
value=iter(numbers)
item1=next(value)
print(item1)
item2=next(value)
print(item2)

######################
def a_function():
    print('a function')
def b_function():
    print("b_function")
a_function()    

def turn_into_b_function(func):
    return b_function 

@ turn_into_b_function
def a_function():
    print('a function')
def b_function():
    print("b_function")
    
a_function() 
################################
def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [5, 3, 8, 6, 7, 2]
sort(nums)
nums
###############################

lst=[5, 3, 8, 6, 7, 2]
def sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    return lst           
                    
          
                
print(sort(lst))               

###########################################
lst=[5, 3, 8, 6, 7, 2]
def i_sort(lst):
    for i in range(1,len(lst)):
        j=i
        while(lst[j-1]>lst[j] and j>0):
            lst[j-1],lst[j] =lst[j],lst[j-1]
            j=j-1
    return lst       
            

print(i_sort(lst))       
#################################
lst=[5, 3, 8, 6, 7, 2]
def i_sort(lst):
    for i in range(1,len(lst)):
        j=i
        while(lst[j-1]>lst[j] and j>0):
              lst[j-1],lst[j]=lst[j],lst[j-1]
              j=j-1
    return lst         

print(i_sort(lst)) 
#############################
lst=["x","y","z","z"]
lst=list(dict.fromkeys(lst))
lst
