#nat 5 way 
import random 

print("Hello, and welcome to the number recognising program, the program will now generate 100 different numbers!")

numbers = [random.randint(0,100) for count in range(0,100)]
count = 0 
for leo in numbers:
    if leo > 80:
        count = count + 1  
print(numbers)
print("The total number of values over 80 is:", count)
