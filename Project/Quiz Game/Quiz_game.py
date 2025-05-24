# Define a function to display the quiz
def run_quiz():
    print("🎓 Welcome to the Basic Python Quiz!")
    print("------------------------------------")
    
    # List of questions (each question is a dictionary)
    questions = [
        {
            "question": "1. What is the capital of Japan?",
            "options": ["A. Tokyo", "B. Beijing", "C. Seoul", "D. Bangkok"],
            "answer": "A"
        },
        {
            "question": "2. What is 10 / 2?",
            "options": ["A. 2", "B. 5", "C. 10", "D. 20"],
            "answer": "B"
        },
        {
            "question": "3. Which data type is used for text in Python?",
            "options": ["A. int", "B. float", "C. str", "D. bool"],
            "answer": "C"
        },
        {
            "question": "4. What keyword defines a function in Python?",
            "options": ["A. def", "B. func", "C. define", "D. function"],
            "answer": "A"
        },
        {
            "question": "5. Which symbol is used to comment in Python?",
            "options": ["A. //", "B. #", "C. <!-- -->", "D. /* */"],
            "answer": "B"
        }
    ]

    # Track score
    score = 0

    # Loop through each question
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        # Get user input
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Check if correct
        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer is {q['answer']}.")

    # Final result
    print("\n🎉 Quiz Complete!")
    print(f"Your score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"That's {percentage:.1f}% correct.")

# Run the quiz
run_quiz()
