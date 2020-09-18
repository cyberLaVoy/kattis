
input() # discard number of people

group = input().split()
group = [int(x) for x in group]

rolls = {}

for roll in group:
    if roll not in rolls:
        rolls[roll] = 1
    else:
        rolls[roll] += 1

unique = []
for roll in rolls:
    if rolls[roll] == 1:
        unique.append(roll)

if len(unique) == 0:
    print("none")
else:
    maxUnique = max(unique)
    for i in range(len(group)):
        if group[i] == maxUnique:
            print(i+1)
            break

