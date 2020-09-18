import random

r = 1000
c = 1000
print(r, c)

for i in range(r):
    row = ""
    for j in range(c):
        num = random.randrange(0,100)
        if num < 10:
            num = 0
        else:
            num = 1
        row += str(num)
    print(row)

numMoves = 1000
print(numMoves)
for i in range(numMoves):
    x1 = random.randrange(1,c+1)
    y1 = random.randrange(1,r+1)
    x2 = random.randrange(1,c+1)
    y2 = random.randrange(1,r+1)
    print(x1, y1, x2, y2)