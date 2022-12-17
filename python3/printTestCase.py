import random

numJewels = 1000000
maxCapacity = 100000
print(numJewels, maxCapacity)
for i in range(numJewels):
    size = random.randrange(1, 100)
    value = random.randrange(1, 1000)
    print(size,value)