# Define a list of quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["1. Berlin", "2. Paris", "3. Rome"],
        "answer": 2
    },
    {
        "question": "What is 2 + 2?",
        "choices": ["1. 3", "2. 4", "3. 5"],
        "answer": 2
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["1. Charles Dickens", "2. William Shakespeare", "3. Jane Austen"],
        "answer": 2
    }
]

score = 0  # Initialize the score

# Loop through each question
for q in questions:
    print("\n" + q["question"])  # Print the question
    for choice in q["choices"]:  # Print the choices
        print(choice)

    try:
        user_answer = int(input("Enter the number of your answer: "))  # Get the user's answer
        if user_answer == q["answer"]:  # Check if the answer is correct
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was:", q["choices"][q["answer"] - 1])
    except ValueError:
        print("Invalid input! Please enter a number.")

# Display the final score
print(f"\nYou scored {score}/{len(questions)}.")