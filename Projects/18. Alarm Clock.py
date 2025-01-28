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
                return days,hours,minutes,seconds

        except ValueError:
                print("Man, I said to enter a number not bs.")

def set_alarm(ddhhmmss):
    
    pass

get_date()

# while True:
#     current_time = d.datetime.now().strftime("%H:%M:%S")
#     print(current_time)
#     time.sleep(1)