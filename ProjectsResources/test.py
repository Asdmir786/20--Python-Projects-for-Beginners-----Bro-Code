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
from pygame import mixer
from keyboard import wait
import pathlib

path = pathlib.Path("ProjectsResources/Audios")
audios = [audio for audio in path.iterdir()]

def set_alarm(user_date="", audio_number = 0):
    parts = user_date.split(":")
    hourss,minutess,secondss = map(int,parts)
    time_to_blyat = d.time(hourss,minutess,secondss)

    while True:
        current_time = d.datetime.now().strftime("%H:%M:%S")
        if current_time == str(time_to_blyat):
            print(f"{current_time} = {time_to_blyat}")
            break
        else:
            print(current_time)
            print(type(current_time))
            time.sleep(1)

set_alarm("23:11:00")