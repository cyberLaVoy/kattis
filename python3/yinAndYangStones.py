
stones = input()
white = 0
black = 0
for stone in stones:
    if stone == 'W':
        white += 1
    else:
        black += 1
if white == black:
    print(1)
else:
    print(0)
