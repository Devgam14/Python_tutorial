import os
import random
def quiz_function (index : int, random_list : list , quiz_bank : list, extracted_questions, scores : float, score_target : float , answers :list , calculated_score_per_ans : float, name : str , question_number : int ):
    """Quiz function logic scoring grading displaying
    Note : Make sure to pass in all the ten arguments below
    Args:
        index (int): Index of the mathematical topic to be quizzed on
        random_list (list): List of random numbers for getting random questions
        quiz_bank (list): Question bank list that is imported
        extracted_questions (list): List of questions that was generated from the question extractor logic
        scores (float): Scores of the individual
        score_target (float): Target of the score 
        answers (list): Answer list for user's answer comparison
        calculated_score_per_ans (float): score per answer
        name (str): users name
    """
    ## Getting random number
    answer_counter = 0
    appraisal_list = ["Wow", "Beautiful", "Excelent" , "Oustanding", "Nice" , "Good" , "Encouraging"]
    for number in random_list:
                question_obj = quiz_bank[index][number - 1]
                extracted_questions.append(question_obj)
    # ask questions and score
    for index, question_obj in enumerate(extracted_questions):
                question_text = question_obj["question"]
                correct_answer = question_obj["answer"]
                response = input(f"{index + 1}. {question_text}\n")
                answers.append(response)
                if int(response) == int(correct_answer):
                    scores += calculated_score_per_ans
                    answer_counter += 1
                    print(f"{random.choice(appraisal_list)}")
                else :
                    print("Ohhh you can do better")
    ##Score grading
    print(f"Youve answerd {answer_counter}/{question_number} questions correctly")
    if scores >= score_target:
                print(f"Congratulations {name} you smashed all the question keep it up and keep going")
                
    elif scores <= 90:
                print(f"Youve done a great job {name} work harder next time dear {name}")
    elif scores <= 60:
                print(f"Congratulations to you you passes pls do better nect time you can do better")
    else :
         print(f" My dear {name} you tried pls do better next time ")
    print(f"Name : {name} \nFinal score: {int(scores)}") 
