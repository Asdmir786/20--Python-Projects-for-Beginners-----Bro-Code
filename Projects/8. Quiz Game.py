import json
import time
import os

# Load the questions from the json file
input_filepath = "C:\\Users\\asmir\\Documents\\20--Python-Projects-for-Beginners-----Bro-Code\\Projects Resources\\quiz-data.json"
with open(input_filepath, "r",encoding="utf-8") as file:
    quiz_data = json.load(file)

total_count = len(quiz_data)

print(total_count)