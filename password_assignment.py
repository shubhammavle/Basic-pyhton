# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:37:26 2023

@author: Dell
"""

users=["admin","employee","manager","worker","staff"]
for user in users:
    if user=="admin":
        print("Hello admin, would you like to see a status report?")
    elif user=="employee":
        print("hello employee")
    elif user=="manager":
        print("hello manager")
    elif user=="worker":
        print("hello worker")
    else:
        print("hello")
##########################################
current_users=["ali","ahmed","fahad","aun","rana"]
new_users=["ali","rana","bilal","huzi","dula"]
for new_user in new_users:
    if new_user in current_users:
        print("person will need to enter a new username.")
    else:
        print("  saying that the username is available..")
########################################
import hashlib
hashlib.sha256("RadhaKrishna@123".encode('utf-8')).hexdigest()
'9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
len(hashlib.sha256("RadhaKrishna@123".encode('utf-8')).digest())
#32

import hashlib
hashlib.sha512("RadhaKrishna@123".encode('utf-8')).hexdigest()
'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff'
len(hashlib.sha512("RadhaKrishna@123".encode('utf-8')).digest())
#64