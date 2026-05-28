# Main routine
print("👨‍🏫👨‍🏫 Welcome to my math quiz 👨‍🏫👨‍🏫")

import random


def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please choose a valid option from the following list {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:

            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()


def make_statement(statement, decoration):

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


def instruction():

    make_statement("Instructions", "ℹ️")

    print("""
Choose Plus / Minus / Divide / Times and try to win
    """)

def get_number(question):

    while True:

        response = input(question).lower()

        if response == "xxx":
            print("You stopped the game")
            exit()

        try:
            return int(response)

        except ValueError:
            print("Please enter a number or 'xxx' to quit.")


# Game Variables
basic_facts = ("plus", "minus", "divide", "times", "xxx")

want_instructions = string_checker("Do you want to see the instructions? ")

if want_instructions == "yes":
    instruction()

print(f"You chose {want_instructions}")

user_choice = string_checker("Choose: ", basic_facts)
print("You chose:", user_choice)

if user_choice == "xxx":
    exit()

score = 0
questions_asked = 5
game_history = []

for question in range(questions_asked):

    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)

    if user_choice == "plus":
        answer = num_1 + num_2
        user_answer = get_number(f"What is {num_1} + {num_2}? ")

    elif user_choice == "minus":
        answer = num_1 - num_2
        user_answer = get_number(f"What is {num_1} - {num_2}? ")

    elif user_choice == "times":
        answer = num_1 * num_2
        user_answer = get_number(f"What is {num_1} x {num_2}? ")

    else:
        answer = random.randint(1, 12)
        num_2 = random.randint(1, 12)
        num_1 = answer * num_2

        user_answer = get_number(f"What is {num_1} ÷ {num_2}? ")

    if user_answer == answer:
        print("Correct! ✅")
        score += 1
        game_history.append("Correct ✅")

    else:
        print(f"Wrong ❌ The answer was {answer}")
        game_history.append(f"Wrong ❌ (Answer: {answer})")

print(f"\nYou got {score} out of {questions_asked} correct!")

see_history = string_checker("\nDo you want to see your game history? ")

if see_history == "yes":

    make_statement("Game History", "=")

    for i in range(len(game_history)):
        print(f"Question {i + 1}: {game_history[i]}")

questions_correct = score
questions_wrong = questions_asked - score

percent_correct = (questions_correct / questions_asked) * 100
percent_wrong = (questions_wrong / questions_asked) * 100

print("\n💎💎💎 Game Statistics 💎💎💎")
print(f"👍 Correct: {questions_correct}")
print(f"😭 Incorrect: {questions_wrong}")
print(f"🎯 Percent Correct: {percent_correct:.2f}%")
print(f"📉 Percent Wrong: {percent_wrong:.2f}%")