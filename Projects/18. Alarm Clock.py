import time
import datetime as d

while True:
    current_time = d.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)