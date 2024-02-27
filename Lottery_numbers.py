# -*- coding: utf-8 -*-
"""
Write python code for random lottery numbers

@author: Dell
"""
from random import randrange
MIN_NUM=1
MAX_NUM=49
NUM_NUMS=6
ticket_nums=[]
for i in range(NUM_NUMS):
    #Generate the number that is not already on the
    #ticket
    rand=randrange(MIN_NUM,MAX_NUM+1)
    while rand in ticket_nums:
        rand=randrange(MIN_NUM,MAX_NUM+1)
    #Add the distinct number to the ticket
    ticket_nums.append(rand)
ticket_nums.sort()
for n in ticket_nums:
    print(n,end="")
    print()