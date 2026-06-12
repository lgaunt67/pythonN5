print("welcome to the 'lets round the number pi to your demand'")

pi = 3.141592653589793

demand = int(input(f"To which place would you like the program to round {pi} to? (max 10 places): "))

if 0 <= demand <= 10:
    print(round(pi, demand))
else:
    print("Please enter a number from 0 to 10.")
