print("Welcome to leap year")

def is_leap_year():
   year=int(input("Enter the year"))
   if((year>0) and (year%4==0) ):
      if (year%100==0):
         if (year%400==0):
            print("Its leap year")
         else:
            print("It is not leap year")  
      else:
           print("It is leap year")
   else:
        print("It is not leap year")
      


   
   
   

is_leap_year()