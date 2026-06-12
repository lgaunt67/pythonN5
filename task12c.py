# question 2b )
print("this will calculate the speed ")
distance = float(input("what is the distance travelled ? "))
time = float(input("what is the time taken to travel that distance? "))
speed = distance / time
print(round(speed,2))

# question 2c )
print("this will calculate your average score on your 3 tests")
test1 = float(input(" what score out of 100 did you get on your math test ? "))
test2 = float(input(" what score out of 100 did you get on your english test ? "))
test3 = float(input(" what score out of 100 did you get on your science test ? "))
averagescore = (test1 + test2 + test3) 
Totalscore = averagescore / 3 
print(round(averagescore,2 ))

# question 2d )
print("this will calculate your 20% discount on your bought item  ")
pop = float(input("what was the full price of the product you bought ?" ))
discount = pop * 0.80
savings = pop - discount
print(round("your final price is", discount,2))
print(round("and your saving £", savings, 2))

