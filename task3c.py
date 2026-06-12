print("This will calculate how much you owe back to the bank each month!")

amount = float(input("How much money did you borrow from the bank? "))
number_of_months = int(input("How many months would you like to repay the loan over? "))

monthly_payment = (amount / number_of_months) * 1.15 

print(f"The amount you will owe each month is £{monthly_payment:.2f}")



