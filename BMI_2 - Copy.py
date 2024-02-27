'''
Write python code to calulate BMI of a person using if elif.
@author:Radhakrishna
'''


height=float(input("please enter your height in m:  "))
weight=float(input("please enter your weight in kg: "))
BMI=round((weight/(height*height)),2)
if BMI<18.5:
    print(f"You are under weight and your BMI is:{BMI}")
elif BMI>18.5 and BMI<25:
    print(f"you are normal weight and your BMI is:{BMI}")
elif BMI>25 and BMI<30:
    print(f"you are over weight and your BMI is:{BMI}")
elif BMI>30 and BMI<35:
    print(f"you are obese and your BMI is:{BMI}")
elif BMI>35:
    print(f"you are clinically obese and your BMI is:{BMI}")