for number in range(1, 7):
    
   
    for dots in range(6 - number):
        print(".", end="")
        
    
    print(number, end="")
   
    for dots in range(number - 1):
        print(".", end="")
        
    print()