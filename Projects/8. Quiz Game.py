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
            user_score += 1
            correct_questions.append(f"{i}. {question}")
        else:
            wrong_questions.append(f"{i}. {question}")
            pass        

    return user_score

user_score = QuizQnA()

total_score = f"{user_score}/{len(quiz_answer)}"

if (user_score/len(quiz_answer))*100 == 100:
    print(f"Total Score: {user_score}/{quiz_answer}\nGudh.")
elif (user_score/len(quiz_answer))*100 == 90:
    print(f"Total Score: {user_score}/{quiz_answer}\nFr Fr.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 == 80:
    print(f"Total Score: {user_score}/{quiz_answer}\nChale Ga.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 == 70:
    print(f"Total Score: {user_score}/{quiz_answer}\nAchi koshish krna.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 == 60:
    print(f"Total Score: {user_score}/{quiz_answer}\nkela kha.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 == 50:
    print(f"Total Score: {user_score}/{quiz_answer}\nBhaiya G ye 50 50 nhi chale ga.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 == 40:
    print(f"Total Score: {user_score}/{quiz_answer}\nBeta tu maut ka khel khel rha hai.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 == 30:
    print(f"Total Score: {user_score}/{quiz_answer}\nTere L lag gye.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 == 20:
    print(f"Total Score: {user_score}/{quiz_answer}\nSai raste me hai or sigma ban.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 >= 10:
    print(f"Total Score: {user_score}/{quiz_answer}\nNikal kele.")
    print(f"{wrong_questions}\n You got these one wrong.")
elif (user_score/len(quiz_answer))*100 == 0:
    print("Beta tughe kia hi bataun tu putr chuti kar.")
    