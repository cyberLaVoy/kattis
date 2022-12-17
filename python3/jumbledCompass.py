
current = int(input())
desired = int(input())

if current < desired:
    clockwise = abs(current-desired)
    counterClockwise = 360 - clockwise
else:
    counterClockwise = abs(current-desired)
    clockwise = 360 - counterClockwise

if clockwise < counterClockwise:
    print(clockwise)
elif counterClockwise < clockwise:
    counterClockwise = 0 - counterClockwise
    print(counterClockwise)
else:
    print(180)
