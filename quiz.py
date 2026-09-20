questions = [
    "What is the capital of India?",
    "Which planet is known as the Red Planet?",
    "What is the extension of a Python file?"
]

options = [
    ["Mumbai", "Delhi", "Kolkata", "Chennai"],
    ["Earth", "Mars", "Jupiter", "Venus"],
    [".py", ".java", ".html", ".txt"]
]

correct_answers = [2, 2, 1]
play_again = "yes"

while play_again == "yes":

    score = 0

    for i in range(len(questions)):
        print(questions[i])

        for number, option in enumerate(options[i], 1):
            print(number, ".", option)

        answer = int(input("Enter your answer (1-4): "))

        if answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", options[i][correct_answers[i] - 1])


    print("Quiz completed!")
    print("Your score:", score, "/", len(questions))
    play_again = input("Do you want to play again? (yes/no): ").lower()