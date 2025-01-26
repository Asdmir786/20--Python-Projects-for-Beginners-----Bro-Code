import time
import datetime as d

def get_date():
    while True:
        user_input = input("Enter the time to BLYAAAT your OS(hh:mm:ss): ")
        parts = user_input.split(":")
        if len(parts) != 3:
            print("Enter with this pattern hh:mm:ss: ")
        else: break
    print(parts)

# while True:
#     current_time = d.datetime.now().strftime("%H:%M:%S")
#     print(current_time)
#     time.sleep(1)