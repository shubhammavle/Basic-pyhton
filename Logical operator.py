'''
Write python code using logical operators and  if elif.so as to check height as well as
so as to allow for roller coster also ask user age and
charge ticket accordingly
@author:Radhakrishna
'''


print("Welcome to the roller coaster")
height=int(input("please enter your height in cm"))
if height>=120:
    print("You are eligible for roller coaster")
    age=int(input("Enter your age in years"))
    bill=0
    if age<12:
        print("child's ticket is 5$")
        bill=5
    elif age>12 and age<18:
         print("youths ticket is 7 $")
         bill=7
    elif age>=18 and age <45:
          print("youngs ticket is 12 $")
          bill=12
    elif age>=45 and age <=55:
        print("Adults ticket is 50 $")
        bill=50
    want_photo=input("Do you want photo Y or N  :")
    if want_photo=='Y':
        bill+=3
        print(f"You need to pay {bill} in $")
    else:
        print(f"You need to pay {bill} in $")

        