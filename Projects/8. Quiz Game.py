import json
import time
import os

# Load the questions from the json file
input_filepath = "C:\\Users\\asmir\\Documents\\20--Python-Projects-for-Beginners-----Bro-Code\\Projects Resources\\quiz-data.json"
with open(input_filepath, "r", encoding="utf-8") as file:
    quiz_data = json.load(file)

correct_questions = []
wrong_questions = []

def QuizQnALogic():
    total_count = len(quiz_data)
    user_score = 0
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
        
            if user_input == " " or user_input == "" or len(user_input) > 1 or user_input not in ["A", "B", "C", "D"]:
                print("Invalid Answer! Try Again.")
            else:
                break
            
        quiz_answer = quiz_answer_full.split()[0][0]
        
        if user_input == quiz_answer:
            user_score += 1
            correct_questions.append(f"{i}. {question}")
        else:
            wrong_questions.append(f"{i}. {question}")

    return user_score, total_count  # Fixed return values

def result(user_score, total_count):  # Fixed function parameters
    percentage = (user_score / total_count) * 100  # Fixed percentage calculation

    if percentage == 100:
        print(f"Total Score: {user_score}/{total_count}\nGudh.")
    elif percentage >= 90:
        print(f"Total Score: {user_score}/{total_count}\nFr Fr.")
    elif percentage >= 80:
        print(f"Total Score: {user_score}/{total_count}\nChale Ga.")
    elif percentage >= 70:
        print(f"Total Score: {user_score}/{total_count}\nAchi koshish krna.")
    elif percentage >= 60:
        print(f"Total Score: {user_score}/{total_count}\nkela kha.")
    elif percentage >= 50:
        print(f"Total Score: {user_score}/{total_count}\nBhaiya G ye 50 50 nhi chale ga.")
    elif percentage >= 40:
        print(f"Total Score: {user_score}/{total_count}\nBeta tu maut ka khel khel rha hai.")
    elif percentage >= 30:
        print(f"Total Score: {user_score}/{total_count}\nTere L lag gye.")
    elif percentage >= 20:
        print(f"Total Score: {user_score}/{total_count}\nSai raste me hai or sigma ban.")
    elif percentage >= 10:
        print(f"Total Score: {user_score}/{total_count}\nNikal kele.")
    else:  # Covers percentage < 10, including 0
        print(f"Total Score: {user_score}/{total_count}\nBeta tughe kia hi bataun tu putr chuti kar.")
    
    if percentage < 100:
        print(f"{wrong_questions}\nYou got these ones wrong.")

def main():
    user_score, total_count = QuizQnALogic()  # Fixed function call
    result(user_score, total_count)  # Fixed function call

main()