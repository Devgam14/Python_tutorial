from logic import logic, terminal_clear
import os

while True:
    counter = 0
    score_counter = 0
    score_target = 100

    print("Welcome to Quiztron")

    name = input("Enter your name >>> ").strip()
    if name == "" :
        print("Pls Enter your name ")
        terminal_clear()
        continue
    elif name.isdigit() :
        print("Enter your name pls")
        terminal_clear()
        continue
    age = input("Enter your age >>> ").strip()

    # AGE VALIDATION (
    if not age.isdigit():
        terminal_clear()
        print("Please enter your age in digits only")
        continue

    age = int(age)

    if age > 5:
        terminal_clear()
        print("Sorry, you are older than the required age\n")
        continue

    question_amount = input(
        "Enter the amount of questions you want to answer in numbers >>> "
    ).strip()

    if not question_amount.isdigit():
        terminal_clear()
        print("Please enter the question amount as digits")
        continue

    number_of_question = int(question_amount)

    if number_of_question == 0:
        terminal_clear()
        print("Question amount cannot be zero")
        continue

    score_per_ans = score_target / number_of_question

    topic = input(
        "Enter the topic you want to be quized on\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        ">>>> "
    ).strip()

    if not topic.isdigit():
        terminal_clear()
        print("Please enter a number between 1 and 4")
        continue

    topic = int(topic)

    if topic == 1:
        terminal_clear()
        print("Addition")
        logic("+", counter, score_counter, score_per_ans, number_of_question, score_target, name)

    elif topic == 2:
        terminal_clear()
        print("Subtraction")
        logic("-", counter, score_counter, score_per_ans, number_of_question, score_target, name)

    elif topic == 3:
        terminal_clear()
        print("Multiplication")
        logic("*", counter, score_counter, score_per_ans, number_of_question, score_target, name)

    elif topic == 4:
        terminal_clear()
        print("Division")
        logic("/", counter, score_counter, score_per_ans, number_of_question, score_target, name)

    else:
        terminal_clear()
        print("Please enter a number from 1 to 4")
