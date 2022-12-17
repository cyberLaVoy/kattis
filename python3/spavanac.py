
time = input().split(' ')
hour = int(time[0])
minute = int(time[1])

if minute >= 45:
    minute = minute - 45 
else:
    hour -= 1
    if hour < 0:
        hour = 24 + hour
    minute = 60 - (45 - minute)

print(hour, minute)