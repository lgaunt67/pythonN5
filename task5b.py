print(" Please select an option from the following menu : ")
print(" 1. Calculate the speed")
print(" 2. Calculate the distance")
print(" 3. Calculate the time")
print(" 4. Calculate the area of a rectangular room")
print(" 5. Exit Program") 
option = int(input(" Please enter the number corresponding to your choice : "))
if option == 1 :
    distance = float(input(" Please enter the distance in meters : "))
    time = float(input(" Please enter the time in seconds : "))
    speed = distance / time 
    print(" The speed is " , speed , " m/s ")
elif option == 2 :
    speed = float(input(" Please enter the speed in m/s : "))
    time = float(input(" Please enter the time in seconds : "))
    distance = speed * time 
    print(" The distance is " , distance , " meters ")
elif option == 3 :
    distance = float(input(" Please enter the distance in meters : "))
    speed = float(input(" Please enter the speed in m/s : "))
    time = distance / speed 
    print(" The time is " , time , " seconds ")
elif option == 4 :
    length = float(input(" Please enter the length of the room in meters : "))
    width = float(input(" Please enter the width of the room in meters : "))
    area = length * width 
    print(" The area of the room is " , area , " square meters ")
elif option == 5 :
    print(" Exiting program... ")
else :
    print(" Invalid option selected. Please try again. ")
    