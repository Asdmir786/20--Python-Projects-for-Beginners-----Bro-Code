import json
import time
import os

# Load the questions from the json file
input_filepath = "C:\\Users\\asmir\\Documents\\20--Python-Projects-for-Beginners-----Bro-Code\\Projects Resources\\quiz-data.json"
with open(input_filepath, "r", encoding="utf-8") as file:
    quiz_data = json.load(file)

correct_answers = []  # Renamed from correct_questions
incorrect_answers = []  # Renamed from wrong_questions

def quiz_logic():  # Renamed from QuizQnALogic
    total_questions = len(quiz_data)  # Renamed from total_count
    score = 0  # Renamed from user_score
    for i in range(1, total_questions + 1):
        quiz_key = f"quiz {i}"
        correct_answer_full = quiz_data[quiz_key]["answer"]  # Renamed from quiz_answer_full
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
            
        correct_answer = correct_answer_full.split()[0][0]  # Renamed from quiz_answer
        
        if user_input == correct_answer:
            score += 1
            correct_answers.append(f"{i}. {question}")
        else:
            incorrect_answers.append(f"{i}. {question}")

    return score, total_questions  # Renamed return values

def display_result(score, total_questions):  # Renamed from result
    percentage = (score / total_questions) * 100  # Fixed percentage calculation

    if percentage == 100:
        print(f"Total Score: {score}/{total_questions}\nGudh.")
    elif percentage >= 90:
        print(f"Total Score: {score}/{total_questions}\nFr Fr.")
    elif percentage >= 80:
        print(f"Total Score: {score}/{total_questions}\nChale Ga.")
    elif percentage >= 70:
        print(f"Total Score: {score}/{total_questions}\nAchi koshish krna.")
    elif percentage >= 60:
        print(f"Total Score: {score}/{total_questions}\nkela kha.")
    elif percentage >= 50:
        print(f"Total Score: {score}/{total_questions}\nBhaiya G ye 50 50 nhi chale ga.")
    elif percentage >= 40:
        print(f"Total Score: {score}/{total_questions}\nBeta tu maut ka khel khel rha hai.")
    elif percentage >= 30:
        print(f"Total Score: {score}/{total_questions}\nTere L lag gye.")
    elif percentage >= 20:
        print(f"Total Score: {score}/{total_questions}\nSai raste me hai or sigma ban.")
    elif percentage >= 10:
        print(f"Total Score: {score}/{total_questions}\nNikal kele.")
    else:  # Covers percentage < 10, including 0
        print(f"Total Score: {score}/{total_questions}\nBeta tughe kia hi bataun tu putr chuti kar.")
    
    if percentage < 100:
        print(f"{incorrect_answers}\nYou got these ones wrong.")

def main():
    score, total_questions = quiz_logic()  # Renamed function call
    display_result(score, total_questions)  # Renamed function call

main()