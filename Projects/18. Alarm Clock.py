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
            user_audio = input(f"Enter the audio number to choose when the alarm will start to BLYAAT(0 to {len(numbers)-1} enter 'r' for any sound.): ").strip()

            if int(user_audio) >= 0 or int(user_audio) <= len(numbers)-1:
                return int(user_audio)
            else: 
                print(f"Enter a number greater than zero and NOT greater than {len(numbers)-1}.")
        except ValueError:
            if user_audio.lower() == "r":
                return user_audio
            print("Enter a Number or the alphabet 'r' please.")

def set_alarm(user_date="", audio_number=""):
    parts = user_date.split(":")
    hourss,minutess,secondss = map(int,parts)
    time_to_blyat = d.datetime.strptime(f"{hourss}:{minutess}:{secondss}","%H:%M:%S")
    once = True
    
    if audio_number.isdigit() == True:
        audio_number = int(audio_number)
    else:
        audio_number = random.randint(0, (len(audios)-1) )

    while True:
        current_time = d.datetime.now().strftime("%H:%M:%S")
        current_time = d.datetime.strptime(current_time, "%H:%M:%S")

        if once == True:
            wait_time = current_time - time_to_blyat
            if wait_time.total_seconds() < 0:
                wait_time = d.timedelta(days=1)
            print(f"Waiting time is: {wait_time}")
            once = False

        if current_time == time_to_blyat:
            mixer.init()
            mixer.music.load(f"{audios[audio_number]}")
            mixer.music.play(-1)

            print("Press Enter to stop the alarm.")
            wait("enter")
            mixer.music.stop()
            print("The Alarm has been stopped. ")
            time.sleep(0.7)
            return True
        else:
            print(current_time.strftime("%H:%M:%S"))
            print(type(current_time))
            time.sleep(1)

def main():
    user_date = get_date()
    user_audio_choice = get_audio()
    set_alarm(user_date,user_audio_choice)

if __name__ == "__main__":
    main()

    while True:
        user_choice = input("Do you want to set another alarm? (y/n): ").lower().strip()
        if user_choice == 'y':
            os.system("cls")
            main()
        elif user_choice == 'n':
            os.system("cls")
            print("Dare I say, but frfr.")
            time.sleep(1)
            exit()
        else:
            print("Enter \"y\" or \"n\" or BOOOOOOOOOOOOOOOOOM!, I will delete that System32 folder if you try me again.")
            
            
        
# Optional Tasks:

# TODO: Snooze Feature
# 1. When alarm triggers, detect 's' keypress to snooze instead of stopping.
# 2. Add snooze_duration (e.g., 5 minutes) to current alarm time.
# 3. Reset the alarm loop with the new time.
# 4. Limit max snooze attempts (e.g., 3 times).

# TODO: Volume Control
# 1. Add a volume input prompt (0.0 to 1.0).
# 2. Use mixer.music.set_volume(volume) before playing.
# 3. Validate input to ensure it's between 0 and 1.

# TODO: Auto-Stop After Duration
# 1. Add a prompt for alarm duration (minutes).
# 2. Start a timer when the alarm begins playing.
# 3. Stop mixer.music after the duration elapses.
# 4. Handle early user interruption (Enter key) as before.

# TODO: Custom Messages
# 1. Add input prompt for a message (e.g., "Meeting at 10 AM!").
# 2. Store the message in a variable.
# 3. Print the message when the alarm triggers.

# TODO: Progress Visualization
# 1. Calculate time remaining until alarm.
# 2. Display dynamic countdown (HH:MM:SS) in the terminal.
# 3. Overwrite the previous line each second for a clean look.
# 4. Stop countdown when alarm triggers or user exits.