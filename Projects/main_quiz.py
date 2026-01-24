### importing the questions
from questions import quiz_bank
import random
from quiz_logic import quiz_function
random_list: list = []
score_target : int = 100
scores : float= 0
calculated_score_per_ans : float= 0
while True : 
    print("Welcome to Quixxy \nPls follow the instaructions below to proceed")
    name = input("What is your name : ").strip()
    if name == "":
        print("Pls enter your name")
        continue
    age = int(input("Enter your age : ").strip())
    if age == "" :
        print("Pls enter your age")
    question_number = int(input("How many questions do you want to answer : "))
    calculated_score_per_ans =  score_target / question_number
    print(calculated_score_per_ans)
    ### generating the random number using the random module
    random_list = random.sample(range(1, len(quiz_bank[0]) + 1), question_number)
    print(random_list)
    extracted_questions:list = []
    answers:list = []
    while True :
        print("Enter the topic you want to be quizzed on \n1. Addition \n2. Subtraction \n3  Multiplication \n4. Division \nEnter your option below to proceed")
        subject_input = int(input(""))
        if subject_input == 1 :
           print("1. Addition:\n")
           quiz_function(0 , random_list, quiz_bank , extracted_questions, scores, score_target , answers , calculated_score_per_ans, name , question_number ) 
           subject_input = 0
           print(f"Bye {name.upper()} \nSee you next time")
           exit()
        elif subject_input == 2 :
            print("2 Subtraction")
            quiz_function(1 , random_list, quiz_bank , extracted_questions, scores, score_target , answers , calculated_score_per_ans, name , question_number ) 
            subject_input = 0
            print(f"Bye {name.upper()}\nSee you next time")
            exit()
        elif subject_input == 3:
            print("3 multiplication")
            quiz_function(2 , random_list, quiz_bank , extracted_questions, scores, score_target , answers , calculated_score_per_ans, name , question_number )
            subject_input = 0
            print()
            print(f"Bye {name.upper()}\nSee you next time")
            exit()
        elif subject_input == 4 :
            print("4 division")
            quiz_function(3 , random_list, quiz_bank , extracted_questions, scores, score_target , answers , calculated_score_per_ans, name  , question_number) 
            subject_input = 0
            print()
            print(f"Bye {name.upper()}\nSee you next time")
            exit()
        else :
            print("Pls enter a number from 1-4 \nTry again")
            continue