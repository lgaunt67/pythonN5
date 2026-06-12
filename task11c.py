valid = False

name = input("What is your name? ")

while valid == False:

    print("What year of High School are you in?")
    year = input()

    if year == "1st" or year == "2nd" or year == "3rd" or year == "4th" or year == "5th" or year == "6th":

        valid = True
        print("Hello", name)
        print("You are in", year, "year.")
        print("Input is valid")

    else:

        print("Invalid year.")
        print("Please enter: 1st, 2nd, 3rd, 4th, 5th, or 6th")