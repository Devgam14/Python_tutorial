import random 
import os
import operator
from random_number_logic import quiz_logic , generate_number_quiz
def terminal_clear () : 
    os.system("cls" if os.name == "nt" else "clear")
score_target: int =  100
number_store = []
score_counter = 0
scores = 0

while True:
    print("Welcome to Quiztron")
    name = input("Enter your name >>> ")
    age = int(input('Enter your age >>>  '))
    if age > 5 :
        print("Please you are older than the required age \n")
        terminal_clear()
        continue
    question_amount = input("Enter the amount of questions you want to answer in numbers >>>  ")
    if question_amount.isalpha() :
        print("Pls enter a digit")
        terminal_clear()
        break
        continue
    number_of_question = int(question_amount)
    score_per_answer = score_target / number_of_question
    ## Generating the random number in twos because it is two
    generate_number_quiz(number_store,number_of_question)
    quiz_logic (number_store , operator.add , score_counter , scores ,score_per_answer , name , score_target , question_amount )
    