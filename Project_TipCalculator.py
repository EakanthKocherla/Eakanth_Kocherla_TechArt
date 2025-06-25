                                                                        #########################
                                                                        # TIP CALCULATOR PROJECT#
                                                                        #########################

# This program calculates the total amount each person should pay when splitting a bill, including a tip.
# It prompts the user for the total bill amount, the tip percentage, and the number of people to split the bill.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? % "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
Final_Amount = round(bill_per_person, 2)
print(f"Each Person Should Pay: {Final_Amount}/-" + ", Please Check the Details Before Paying")
print ("** Thankyou Visit Again **")