# import datetime as d 

# days = 1
# hours = 12
# minutes = 42
# seconds = 58

# current_time = d.datetime.now().strftime("%d %H:%M:%S")
# user_date = d.datetime.now().replace(day=days,hour=hours,minute=minutes,second=seconds,microsecond=0).strftime("%d %H:%M:%S")

# print(current_time)
# print("="*12)
# print(user_date)
import datetime as d
import time
# from keyboard import wait
# import pathlib

# path = pathlib.Path("ProjectsResources/Audios")
# audios = [audio for audio in path.iterdir()]

# def set_alarm(user_date="", audio_number = 0):
#     parts = user_date.split(":")
#     hourss,minutess,secondss = map(int,parts)
#     time_to_blyat = d.time(hourss,minutess,secondss)

#     while True:
#         current_time = d.datetime.now().strftime("%H:%M:%S")
#         if current_time == str(time_to_blyat):
#             print(f"{current_time} = {time_to_blyat}")
#             break
#         else:
#             print(current_time)
#             print(type(current_time))
#             time.sleep(1)

# set_alarm("23:11:00")

# now = d.datetime.now().strftime("%H:%M:%S")

# while True:
#     time.sleep(0.1)
#     new_now = d.datetime.now().strftime("%H:%M:%S")

#     if new_now == now:
#         print(f"{now} : {new_now} are Same.")   
#     else:
#         print(f"{now} : {new_now}")
#         now = d.datetime.now().strftime("%H:%M:%S")

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt6.QtCore import QTimer, Qt

# app = QApplication(sys.argv)

# # Create a main window and a label to display the counter
# window = QMainWindow()
# window.setWindowTitle("Counter Timer")
# label = QLabel("0")
# label.setAlignment(Qt.AlignmentFlag.AlignCenter)
# window.setCentralWidget(label)
# window.resize(200, 100)
# window.show()

# counter = 0

# def update_counter():
#     global counter
#     counter += 1
#     label.setText(str(counter))

# # Set up a timer that calls update_counter every 1000ms (1 second)
# timer = QTimer()
# timer.timeout.connect(update_counter)
# timer.start(1000)

# sys.exit(app.exec())

import requests
import datetime

# Replace with your actual API key
api_key = "384a7841f7fdedeb6bbff308c6d50713"
city = "Lahore"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send the request
response = requests.get(url)
data = response.json()

# Extract relevant details
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
weather_code = data["weather"][0]["id"]

# Instead of mapping weather code to an emoji, use the provided icon code
icon_code = data["weather"][0]["icon"]  # e.g., "10d" or "01n"
icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

# Create a timezone object using the API's timezone offset (in seconds)
timezone_offset = data["timezone"]
tz_local = datetime.timezone(datetime.timedelta(seconds=timezone_offset))

# Convert Unix timestamps to local time using datetime.fromtimestamp() with tz parameter
current_time_local = datetime.datetime.fromtimestamp(data["dt"], tz=tz_local)
# The sunrise and sunset values are used to help determine if it's day or night
sunrise = data["sys"]["sunrise"]
sunset = data["sys"]["sunset"]

# Determine the time of day
if data["dt"] < sunrise or data["dt"] > sunset:
    time_of_day = "night"
else:
    hour = current_time_local.hour
    if 6 <= hour < 12:
        time_of_day = "morning"
    elif 12 <= hour < 18:
        time_of_day = "afternoon"
    elif 18 <= hour < 21:
        time_of_day = "evening"
    else:
        time_of_day = "daytime"

# Print the collected information
# print(f"Temperature: {temperature} °C")
# print(f"Feels like: {feels_like} °C")
# print(f"Description: {description}")
# print(f"Weather code: {weather_code}")
# print(f"Current local time: {current_time_local.strftime('%Y-%m-%d %H:%M:%S')}")
# print(f"It's currently: {time_of_day}")
# print(f"Weather icon URL: {icon_url}")
print(data["cod"])

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Input Example")
#         self.resize(300, 100)

#         # Create an input bar (QLineEdit)
#         self.input_line = QLineEdit(self)
#         self.input_line.setPlaceholderText("Type something...")

#         # Create a button to capture the input text
#         self.button = QPushButton("Submit", self)
#         self.button.clicked.connect(self.handle_input)

#         # Create a label to display the stored text
#         self.label = QLabel("", self)

#         # Set up a vertical layout and add widgets
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.input_line)
#         layout.addWidget(self.button)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#     def handle_input(self):
#         # Retrieve the text from the input bar
#         user_text = self.input_line.text()
#         # Store and use the text as needed
#         self.label.setText("You entered: " + user_text)
#         print("Stored text:", user_text)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())
