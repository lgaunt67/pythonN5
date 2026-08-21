for pupil in range(1, 6):
    print("Pupil", pupil)
    
    breakfast = int(input("Enter breakfast calories: "))
    lunch = int(input("Enter lunch calories: "))
    dinner = int(input("Enter dinner calories: "))
    
    total = breakfast + lunch + dinner
    
    print("Total calories for the day:", total)