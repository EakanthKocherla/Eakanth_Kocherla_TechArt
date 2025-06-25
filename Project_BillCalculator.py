                                                                        ###########################
                                                                        # Bill CALCULATOR PROJECT #
                                                                        ###########################

# This is a simple bill calculator that takes the total bill amount, tip amount, and number of people to split the bill.
# It calculates the total amount including the tip and divides it by the number of people to find out how much each person should pay.

print("Welcome to the Bill calculator!")
bill = float(input("What was the total bill? Rs: "))
tip = float(input("What was the total tip paid? Rs: "))
people = int(input("How many people to split the bill? "))
Total_Amount = bill + tip
print (f"The total bill including the tip is Rs: {Total_Amount}")
Calculations = (Total_Amount / people)
Final_Amount = round(Calculations, 2)
print (f"The Total Amount was shared between {people} members.")
print (f"Each Person Should Pay: {Final_Amount}/- " + "Please Check the Details Before Paying")
print ("** Thankyou Visit Again **")