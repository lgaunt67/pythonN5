print("Hello , welcome to the quessing number game !")
import random 
number = random.randint(1, 100)
guess = -1

while guess != number:
    guess = int(input("Please enter a number between 1 and 100 :"))
    if guess < number:
        print("too low, try again")
    elif guess > number:
        print("too high, try again")
    else:
        print("congratulations, you guessed the number !")
    


