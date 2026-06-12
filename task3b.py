print(" This program will calculate how much each person at the table will have to pay for the meal including the tip") 
number_of_people = int(input(" how many people were at the table having the meal ? "))
total_cost = float(input(" What was the total cost of the meal ?"))
cost_for_each_person = (total_cost  * 1.1 ) / number_of_people 
print("the cost for each person at the table is " , cost_for_each_person ) 