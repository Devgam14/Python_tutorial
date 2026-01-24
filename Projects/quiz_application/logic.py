import os
import random
import math

def terminal_clear():
    os.system("cls" if os.name == "nt" else "clear")


def logic(operand, count, score_counter, score_per_ans, question_amount, score_target, name):
    appraisals = [
        "Good", "Wonderfull", "Intresting", "Fabulous",
        "Smart kid", "Intelligent kid", "Genuis brain", "Great performance"
    ]

    question_counter = 0
    switcher = True

    while switcher:
        question_counter += 1

        num1 = random.randint(1, 11)
        num2 = random.randint(1, 11)

        if operand == "+":
            question = int(input(f"{num1} + {num2} >>> "))
            answer = num1 + num2

        elif operand == "-":
            question = int(input(f"{num1} - {num2} >>> "))
            answer = num1 - num2

        elif operand == "*":
            question = int(input(f"{num1} * {num2} >>> "))
            answer = num1 * num2

        elif operand == "/":
            num1 = random.randint(6, 11)
            num2 = random.randint(1, 6)
            question = float(input(f"{num1} / {num2} >>> "))
            answer = num1 / num2

        if question == answer:
            count += 1
            score_counter += score_per_ans
            print(random.choice(appraisals))

        print("\nDo you want to continue")
        progress_answer = int(input("0. Quit \n1. Continue\n>>> "))

        if progress_answer == 1:
            terminal_clear()

            if question_counter == question_amount:
                break
            continue

        elif progress_answer == 0:
            print(f"Wow you got {count}/{question_amount}")
            print("I love your effort\nTry again next time")
            exit()

        else:
            print("Pls answer with 0 or 1")

        if question_counter == question_amount:
            switcher = False

    print(f"You've answered {count}/{question_amount} questions correctly")

    if count == question_amount:
        print(f"Congratulations {name} you smashed all the questions")

    elif count > question_amount / 2:
        print(f"You've done a great job {name}, work harder next time")

    else:
        print(f"My dear {name}, you tried. Please do better next time")

    print(f"Name : {name}")
    print(f"Final score: {score_counter}")

    while True:
        continue_question = int(input("Do you want to continue\n0. No\n1. Yes\n>>> "))

        if continue_question == 0:
            terminal_clear()
            exit()

        elif continue_question == 1:
            terminal_clear()
            break

        else:
            terminal_clear()
            print("Enter 0 to stop or 1 to continue")
