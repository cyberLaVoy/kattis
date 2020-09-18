
total = 0
for i in range(64):
    if total >= 3**i:
        print(i)
    total += 3**i