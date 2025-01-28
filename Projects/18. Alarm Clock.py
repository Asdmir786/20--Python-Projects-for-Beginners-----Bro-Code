import time
import datetime as d

def get_date():
    while True:
        user_input = input("Enter the time to BLYAAAT your OS(dd:hh:mm:ss): ")
        parts = user_input.split(":")
        if len(parts) != 4:
            print("Enter with this pattern dd:hh:mm:ss: ")
            continue
        else: 
            pass

        try:
            days,hours,minutes,seconds = map(int,parts)
            if days < 0 or days > 365:
                print("Enter the number of days before 365 or 0 or after 0, who the hell writes negative days?")
            
            elif hours < 0 or hours > 23:
                print("Invalid hours! Please enter a value between 0 and 23.")

            elif minutes < 0 or minutes > 59:
                print("Invalid minutes! Please enter a value between 0 and 59.")
            
            elif seconds < 0 or seconds > 59:
                print("Invalid seconds! Please enter a value between 0 and 59.")
            
            else: 
                print("Valid Input Phinnaly!")
                user_date = d.datetime.now().replace(day=days,hour=hours,minute=minutes,second=seconds,microsecond=0).strftime("%d %H:%M:%S")
                return user_date

        except ValueError:
                print("Man, I said to enter a number not bs.")

def set_alarm(user_date=""):
    parts = user_date.split(":")
    dayss,hourss,minutess,secondss = map(int,parts)
    time_to_blyat = d.datetime.now() + d.timedelta(days=dayss,hours=hourss,minutes=minutess,seconds=secondss)
    time_to_blyat = time_to_blyat.strftime("%d %H:%M:%S")
    while True:
        if current_time != time_to_blyat:
            current_time = d.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            print(type(current_time))
            time.sleep(1)
        else:
            return "WIP"

set_alarm("0 0:0:10")

# while True:
#     current_time = d.datetime.now().strftime("%H:%M:%S")
#     print(current_time)
#     time.sleep(1)