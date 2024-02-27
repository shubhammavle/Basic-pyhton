print("Welcome to the tip calculator")
total_bill=input("how much is the total bill?")
tip=input("how much percentage of tip should be given?")
total_persons=input("how many people are there in dinner?")
total_persons=int(total_persons)
total_tip=float(tip)/100
bill_plus_tip=float(total_bill)+total_tip
per_person_contribution=round(bill_plus_tip/(total_persons),2)
print(f"per person need to give {per_person_contribution} contribution")