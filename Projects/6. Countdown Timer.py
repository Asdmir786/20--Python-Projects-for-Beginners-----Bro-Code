import time

def get_input():
    while True:
        try:
            userTime = int(input(f"Enter your time in seconds: "))
            if userTime <= 0:
                count = 0
                count += 1
                if count < 3:
                    print("Either greater than 1 or bye bye.")
                else:
                    print("TU nhi sudhrega bc")
                    time.sleep(1)
                    exit()
            else:
                break
        except ValueError:
            print("Invalid BS! Number plj")
    return userTime

def main(userTime):
    for time_main in range(userTime, 0, -1):
        seconds = time_main % 60
        minutes = (time_main // 60) % 60
        hours = time_main // 3600
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1.0)

    print("Time's up!")

try:
    user_time = get_input()
    main(user_time)
except KeyboardInterrupt:
    print("\nExiting Fr Fr.")
    exit()
