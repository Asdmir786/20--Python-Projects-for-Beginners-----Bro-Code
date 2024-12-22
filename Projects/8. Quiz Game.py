import json
import time
import os



# Load the questions from the json file
input_filepath = "C:\\Users\\asmir\\Documents\\20--Python-Projects-for-Beginners-----Bro-Code\\Projects Resources\\quiz-data.json"
with open(input_filepath, "r",encoding="utf-8") as file:
    quiz_data = json.load(file)

total_count = len(quiz_data)
quiz_answer = []
user_answer = []
correct_questions = []
wrong_questions = []
user_score = 0

def QuizQnA():
    global user_score
    for i in range(1, total_count + 1):
        quiz_key = f"quiz {i}"
        quiz_answer_full = quiz_data[quiz_key]["answer"]
        question = quiz_data[quiz_key]["question"]
        
        print("<========================================>\n")
        print(f"{i}. {question}")
        for option in quiz_data[quiz_key]["options"]:
            print(option)
            
        while True:
            user_input = input("\nAnswer(A,B,C,D): ").upper().strip()
        
            if user_input == " "  or user_input == "" or len(user_input) > 1 or user_input not in ["A","B","C","D"]:
                print("Invalid Answer! Try Again.")
            else:
                break
            
        quiz_answer.append(quiz_answer_full.split()[0][0])
        user_answer.append(user_input)

        if user_answer == quiz_answer:
            correct_questions.append(f"{i}. {question}")
        else:
            wrong_questions.append(f"{i}. {question}")
            pass        

QuizQnA()
print(f"Correct Questions: {correct_questions},\nWrong Questions: {wrong_questions}")

# for i in range(0, len(quiz_answer)):
#     if user_answer[i] == quiz_answer[i]:
#         user_score += 1
#     else:
#         wrong_questions.append(user_answer[i])
#         pass

# total_score = f"{user_score}/{len(quiz_answer)}"

# print(f"Total Score: {total_score}")