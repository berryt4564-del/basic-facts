

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