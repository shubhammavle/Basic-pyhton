# -*- coding: utf-8 -*-
"""
Password picker

@author: Dell
"""

import string
#Pick the adjectives
adjectives = ['sleepy', 'slow', 'smelly',
'wet', 'fat', 'red',
'orange', 'yellow', 'green',
'blue', 'purple', 'fluffy',
'white', 'proud', 'brave']
#Pick the nouns
nouns = ['apple', 'dinosaur', 'ball',
'toaster', 'goat', 'dragon',
'hammer', 'duck', 'panda']
#Pick the words
import random

adjective = random.choice(adjectives)
noun = random.choice(nouns)
#Select a number
number = random.randrange(0, 100)
#Select a special character
special_char = random.choice(string.punctuation)
#Create the new secure password
password = adjective + noun + str(number) + special_char
print('Your new password is: %s' % password)
#Another one?
#You can use a while loop to generate 
#another
print('Welcome to Password Picker!')
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' % password)
    response = input('Would you like generate another password? Type y or n: ')
    if response == 'n':
       break
