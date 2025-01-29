import time
import datetime as d
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Must be set BEFORE importing pygame
from pygame import mixer
from keyboard import wait
import pathlib
import random

path = pathlib.Path("ProjectsResources/Audios")
audios = [audio for audio in path.iterdir()]

def get_date():
    while True:
        user_input = input("Enter the time to BLYAAAT your OS(hh:mm:ss): ")
        parts = user_input.split(":")
        if len(parts) != 3:
            print("Enter with this pattern hh:mm:ss: ")
            continue
        else: 
            pass

        try:
            hours,minutes,seconds = map(int,parts)
            if hours < 0 or hours > 23:
                print("Invalid hours! Please enter a value between 0 and 23.")

            elif minutes < 0 or minutes > 59:
                print("Invalid minutes! Please enter a value between 0 and 59.")
            
            elif seconds < 0 or seconds > 59:
                print("Invalid seconds! Please enter a value between 0 and 59.")
            
            else: 
                print("Valid Input Phinnaly!")
                user_date = d.datetime.now().replace(hour=hours,minute=minutes,second=seconds).strftime("%H:%M:%S")
                return user_date

        except ValueError:
                print("Man, I said to enter a number not bs.")

def get_audio():
    numbers = []
    while True:
        try:
            for i,audio in enumerate(audios):
                print(f"{i}. {audio}")
                numbers.append(i)
            user_audio = input(f"Enter the audio number to choose when the alarm will start to BLYAAT(0 to {len(numbers)-1} enter 'random' for any sound.): ").strip()

            if int(user_audio) >= 0 or int(user_audio) <= len(numbers)-1:
                return int(user_audio)
            else: 
                print(f"Enter a number greater than zero and NOT greater than {len(numbers)-1}.")
        except ValueError:
            if user_audio.lower() == "random":
                return user_audio
            print("Enter a Number or the word 'random' please.")

def set_alarm(user_date="", audio_number=""):
    parts = user_date.split(":")
    hourss,minutess,secondss = map(int,parts)
    time_to_blyat = d.time(hourss,minutess,secondss)
    if audio_number.isdigit() == True:
        audio_number = int(audio_number)
    else:
        audio_number = random.randint(0, (len(audios)-1) )

    while True:
        current_time = d.datetime.now().strftime("%H:%M:%S")

        if current_time == str(time_to_blyat):
            mixer.init()
            mixer.music.load(f"{audios[audio_number]}")
            mixer.music.play(-1)

            print("Press Enter to stop the alarm.")
            wait("enter")
            mixer.music.stop()
            print("The Alarm has been stopped. ")
            time.sleep(0.7)
            break
        else:
            print(current_time)
            print(type(current_time))
            time.sleep(1)

if __name__ == "__main__":
    user_date = get_date()
    user_audio_choice = get_audio()
    set_alarm(user_date,user_audio_choice)