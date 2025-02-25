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

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QTimer, Qt

app = QApplication(sys.argv)

# Create a main window and a label to display the counter
window = QMainWindow()
window.setWindowTitle("Counter Timer")
label = QLabel("0")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
window.setCentralWidget(label)
window.resize(200, 100)
window.show()

counter = 0

def update_counter():
    global counter
    counter += 1
    label.setText(str(counter))

# Set up a timer that calls update_counter every 1000ms (1 second)
timer = QTimer()
timer.timeout.connect(update_counter)
timer.start(1000)

sys.exit(app.exec())