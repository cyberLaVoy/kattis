import datetime

translation = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

date = input().split()
day = int(date[0])
month = int(date[1])

date = datetime.date(2009, month, day)
dayOfWeek = translation[date.weekday()]
print(dayOfWeek)