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
    
        if user_input == " "  or user_input == "" or len(user_input) > 1:
            print("Invalid!")
        else:
            break
        
    quiz_answer.append(quiz_answer_full.split()[0][0])
    user_answer.append(user_input)


print(quiz_answer)
print(user_answer)