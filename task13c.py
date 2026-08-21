questions = [""] * 5
answers = [""] * 5

questions[0] = "What is the capital of France? "
questions[1] = "What is 12 x 12? "
questions[2] = "What colour is the sky? "
questions[3] = "How many days are in a week? "
questions[4] = "What planet do we live on? "

answers[0] = "paris"
answers[1] = "144"
answers[2] = "blue"
answers[3] = "7"
answers[4] = "earth"

score = 0

for counter in range(0, 5):
    user_answer = input(questions[counter])
    
    if user_answer.lower().strip() == answers[counter]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The answer was", answers[counter])

# Display final score
print("Quiz Complete ")
print("You scored", score, "out of 5")

if score == 5:
    print("Perfect score!")
elif score >= 3:
    print("Well done!")
else:
    print("Better luck next time!")