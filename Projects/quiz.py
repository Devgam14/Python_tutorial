### importing the questions
from questions import quiz_bank
import random
from quiz_logic import quiz_function
random_list: list = []
score_target = 100
scores = 0
calculated_score_per_ans = 0
while True : 
    print("Welcome to Quixxy \nPls follow the instaructions below to proceed")
    name = input("What is your name : ").strip()
    if name == "":
        print("Pls enter your name")
        continue
    age = int(input("Enter your age : ").strip())
    if age == "" :
        print("Pls enter your age")
        continue
    question_number = int(input("How many questions do you want to answer : "))
    calculated_score_per_ans =  score_target / question_number
    print(calculated_score_per_ans)
    random_list = random.sample(range(1, len(quiz_bank[0]) + 1), question_number)
    print(random_list)
    extracted_questions:list = []
    answers:list = []
    while True :
        print("Enter the topic you want to be quizzed on \n1. Addition \n2. Subtraction \n3  Multiplication \n4. Division \nEnter your option below to proceed")
        subject_input = int(input(""))
        if subject_input == 1 :
           print("1. Addition:\n")
           quiz_function(0 , random_list, quiz_bank , extracted_questions, scores, score_target , answers , calculated_score_per_ans, name ) 
        elif subject_input == 2 :
            print("2 Subtraction \n")
            quiz_function(1 , random_list, quiz_bank , extracted_questions, scores, score_target , answers , calculated_score_per_ans, name ) 
        elif subject_input == 3:
            print("3 Multiplication \n")
            quiz_function(2 , random_list, quiz_bank , extracted_questions, scores, score_target , answers , calculated_score_per_ans, name ) 
        elif subject_input == 4 :
            print("4 Division \n")
            quiz_function(3 , random_list, quiz_bank , extracted_questions, scores, score_target , answers , calculated_score_per_ans, name ) 
        else :
            print("Pls enter a number from 1-4 \nTry again")
            continue
        print(subject_input)