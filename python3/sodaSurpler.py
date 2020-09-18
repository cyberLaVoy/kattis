
emptyBottles = input().split()
required = int(emptyBottles[2])
totalEmpty = int(emptyBottles[0]) + int(emptyBottles[1])

totalSodas = 0
while totalEmpty >= required:
    remainder = totalEmpty % required
    totalSodas += totalEmpty//required
    totalEmpty = totalEmpty//required + remainder
print(totalSodas)