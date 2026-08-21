print(" hello , and welcome to the number recognising program, the program will now generate 100 different numbers !")
import random
numbers = [random.randint(0, 100) 
for count in range(100)]
count_over_80 = sum(1 for num in numbers if num > 80)
print("The 100 numbers:")
print(numbers)
print("Amount of numbers over 80:", count_over_80)


