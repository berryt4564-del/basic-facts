# Main routine
print()
print("👨‍🏫👨‍🏫 Welcome to my math quiz👨‍🏫👨‍🏫")
print()

def yes_no(question):
    """check user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y/ n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

def make_statement (statement, decoration):
    """Adds emoji / additional characters"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

def instruction():
    """print instructions"""

    make_statement("Instructions", "ℹ️")

    print("""
    
Choose Plus / Minus / Divide / Times and try to win
    """)

# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

basic_facts = ("Plus", "Minus", "Divide", "Times", "xxx")

def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please choose a valid option from the following list {valid_ans}"

    while True:


        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item


            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item


        print(error)
        print()

# Game Variables
basic_facts = ("plus", "minus", "divide", "times")

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instruction()

print(f"you chose {want_instructions}")

user_choice = string_checker("Choose: ", basic_facts)
print("You chose: ", user_choice)

import random

# Score variables
score = 0
questions_asked = 5

# Ask questions
for question in range(questions_asked):

    # Generate random numbers
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)

    # Plus
    if user_choice == "plus":
        answer = num_1 + num_2
        user_answer = int(input(f"What is {num_1} + {num_2}? "))

    # Minus
    elif user_choice == "minus":
        answer = num_1 - num_2
        user_answer = int(input(f"What is {num_1} - {num_2}? "))

    # Times
    elif user_choice == "times":
        answer = num_1 * num_2
        user_answer = int(input(f"What is {num_1} x {num_2}? "))

    # Divide
    else:
        # Make division questions divide evenly
        answer = random.randint(1, 12)
        num_2 = random.randint(1, 12)
        num_1 = answer * num_2

        user_answer = int(input(f"What is {num_1} ÷ {num_2}? "))

    # Check answer
    if user_answer == answer:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong ❌ The answer was {answer}")

    print()

# Final score
print(f"You got {score} out of {questions_asked} correct!")

# Game History / Statistics area

# check users have played at least one round before calculating statistics!
if rounds_played > 0:

    # Calculate Statistics
    questions_correct = score
    questions_wrong = questions_asked - score

    percent_correct = questions_correct - score
    percent_wrong = questions_wrong / questions_asked

    # Output Game Statistics
    print("💎💎💎 Game Statistics 💎💎💎")
    print (f"👍 Won: {questions_correct:.2f} \t "
           f"😭 Lost: {questions_wrong:.2f} \t "
           f"👔 Tied: {questions_asked:.2f}")

    # ask user if they want to see their game history and output it if requested.
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":

        make_statement("Game History", "=")

        for item in game_history:
            print(item)

        print()
        print("Thanks for playing.")

