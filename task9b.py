print("Hello , welcome to the quessing number game !")
number = 58 
guess = ""

while guess != number:
    guess = int(input("guess a number between 1 and 100 : "))
    if guess < number:
        print("too low, try again")
    elif guess > number:
        print("too high, try again")
    else:
        print("congratulations, you guessed the number !")