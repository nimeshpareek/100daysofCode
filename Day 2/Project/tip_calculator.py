print("Welcome to the tip calculator!!")
bill = float(input("Enter the total bill"))
tip = int(input("How much percentage you want ot give as a tip ?? "))
people = int(input("In how many people you wanna to split the bill ?? "))
tip_percent = tip / 100
total_tip_amount = tip_percent *bill
total_bill = total_tip_amount + bill
bill_per_person = total_bill / people
print(round(bill_per_person, 2))