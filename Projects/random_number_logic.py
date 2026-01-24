import operator
import random
def generate_number_quiz (number_store : list , number_of_question : list) :
       for _ in  range(number_of_question + 1) :
        random_number = random.randint(1 , 11)
        number_store.append(random_number)
def calculate(num1 , num2 , action) :
    return action(num1 , num2)
def quiz_logic (number_store , sign , score_counter , scores ,score_per_answer , name , score_target , question_number  ) : 
    appraisal_list = ["Wow", "Beautiful", "Excelent" , "Oustanding", "Nice" , "Good" , "Encouraging"]
    for num1 , num2  in zip(number_store , number_store[1:]):
        question =input(f"{num1} {sign} {num2}")
        answer : int = calculate(num1 , num2 , operator.add)
        print(f"this is your question {question} this is the answer {answer}")
        score += score_per_answer
        if int(question) == answer :
            score_counter + 1
            print(f"{random.choice(appraisal_list)}")
        else :
            namer.strip()
            print(f"Ohh you can do better next time {name}")
        print(f"Youve answerd {score_counter}/{question_number} questions correctly")
    if scores >= score_target:
                print(f"Congratulations {name} you smashed all the question keep it up and keep going")
                
    elif scores <= 90:
                print(f"Youve done a great job {name} work harder next time dear {name}")
    elif scores <= 60:
                print(f"Congratulations to you you passes pls do better nect time you can do better")
    else :
         print(f" My dear {name} you tried pls do better next time ")
    print(f"Name : {name} \nFinal score: {int(scores)}") 
    
    