print("This is the tip calculator")
bill=float(input("Enter total bill: $"))
tip_percent=int(input("Enter tip percentage: "))
total_bill=bill*(1+tip_percent/100.00)
split=int(input("How many ways is the bill being split?\n"))
per_person=round(total_bill/split,2)
print("Each person should pay: $"+str(per_person))
# calculates the total bill with tip and splits it among a number of people