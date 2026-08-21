StudentName = [""] * 5
test_score = [""] * 5

for counter in range(0, 5):
    StudentName[counter] = input("Enter the name of Student: ")

    test_score[counter] = int(input("Enter the test score out of 150 marks: "))

    while test_score[counter] < 0 or test_score[counter] > 150:
        print("Please enter a valid score between 0 and 150")
        test_score[counter] = int(input("Enter the test score out of 150 marks: "))

# Displaying results
print("Results")

for counter in range(0, 5):
    if test_score[counter] >= 75:
        result = "PASSED"
    else:
        result = "FAILED"

    print(StudentName[counter], "scored", test_score[counter], "out of 150 and", result)