import random 
print(" Welcome to the national lottery, the program will now generate 6 different numbers !")
number1 = random.randint(1, 60) 
number2 = random.randint(1, 60)
number3 = random.randint(1, 60)
number4 = random.randint(1, 60)
number5 = random.randint(1, 60)
number6 = random.randint(1, 60)

while number1 == number2:
    number2 = random.randint(1, 60)
print(number1, number2)
while number1 == number3 or number2 == number3:
    number3 = random.randint(1, 60)
print(number1, number2, number3)
while number1 == number4 or number2 == number4 or number3 == number4:
    number4 = random.randint(1, 60)
print(number1, number2, number3, number4)
while number1 == number5 or number2 == number5 or number3 == number5:
    number5 = random.randint(1,60)
print(number1, number2, number3, number4, number5 )
while number1 == number6 or number2 == number6 or number3 == number6 or number5 == number6:
    number6 = random.randint(1,60)
print(number1, number2, number3, number4, number5, number6)
 