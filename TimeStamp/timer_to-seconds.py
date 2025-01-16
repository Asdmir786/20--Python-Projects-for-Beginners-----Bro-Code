
time = input("Time(hh:mm:ss): ")
times = time.split(":")
times = list(map(int, times))

hours = times[0]*3600
minutes = times[1]*60
seconds = times[2]*1

main_sum = hours+minutes+seconds

print(f"{time} in seconds is {main_sum}s")