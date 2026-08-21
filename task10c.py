for number in range(1, 6):
    
   
    for dots in range(5 - number):
        print(".", end="")
        
    
    print(number, end="")
   
    for dots in range(number - 1):
        print(".", end="")
        
    print()