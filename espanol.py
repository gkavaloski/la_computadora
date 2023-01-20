import random
import spanishdicts


print("How many phrases would you like to practice?")
amount_of_phrases = int(input())

correct_answers = 0
wrong_answers = 0
total_score = 0

for i in range(amount_of_phrases):
    spanish, anglo = random.choice(list(spanishdicts.anglo_spanish.items()))
    print("\n" + anglo + "\n")
    answer = input("~~: ")
    if answer == spanish:
        print("\n" + "." * 26)
        print("Success!!!")
        print("." * 26)
        correct_answers = correct_answers + 1
    else:
        print("\n" + "X" * 26)
        print("Nope. Try: " + spanish)
        print("X" * 26)
        wrong_answers = wrong_answers + 1

if wrong_answers == 0:
    total_score = 100
elif correct_answers == 0:
    total_score = 0
else:
    total_score = round((correct_answers / amount_of_phrases) * 100, 2)

print("\n End of game.")
print(str(correct_answers) + " correct, and " + str(wrong_answers) + " wrong.")
print("Your score is: " + str(total_score) + "%")
    


