print("Welcome to the love score calculator")
name1=input("What is your name?")
name2=input("What is your fiance name")
name1=name1.lower()
name2=name2.lower()
name=name1+name2
t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
true=t+r+u+e

l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
love=l+o+v+e

score=str(true)+str(love)
print(f"The true love score is:{score}")