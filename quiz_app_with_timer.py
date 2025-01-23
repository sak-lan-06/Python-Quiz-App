import random  # Importing the random module for shuffling questions
import time

# Step 1: Define the questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Rome", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which programming language is known as the language of AI?",
        "options": ["Python", "Java", "C++", "Ruby"],
        "answer": "Python"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "10", "12"],
        "answer": "8"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Saturn", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Shark", "Giraffe"],
        "answer": "Blue Whale"
    }
]

# Step 2: Shuffle the questions
random.shuffle(questions)  # Randomizes the order of questions


# Step 3: Define a function to run the quiz
def run_quiz():
    score = 0  # Variable to store the user's score

    print("Welcome to the Quiz App!")
    print("Answer the following questions:\n")

    for i, q in enumerate(questions, start=1):  # Loop through each question
        print(f"Question {i}: {q['question']}")  # Display the question
        for idx, option in enumerate(q['options'], start=1):  # Display the options
            print(f"{idx}. {option}")

        start_time = time.time()
        user_choice = None

        # Step 4: Get the user's answer
        while time.time() - start_time < 5:
            try:
                user_input = input("Enter the option number (1-4): ")  # Get user input
                if user_input.isdigit() and 1 <= int(user_input) <= 4:
                    user_choice = int(user_input)
                    break
                else:
                    print("Invalid choice. Please select a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if user_choice is None:
            print("Time's up! Moving to the next question.\n")

        else:
            selected_option = q['options'][user_choice - 1]
            if selected_option == q['answer']:
                print("Correct!\n")
                score += 1

            else:
                print(f"Wrong! The correct answer is: {q['answer']}\n")

    # Step 6: Display the final score
    print(f"Quiz Over! You scored {score}/{len(questions)}.")


# Step 7: Run the quiz
if __name__ == "__main__":
    run_quiz()