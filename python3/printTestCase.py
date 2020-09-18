import random

numJewels = 1000000
maxCapacity = 301
maxSize = 300
maxValue = 1000000000
print(numJewels, maxCapacity)
for i in range(numJewels):
    size = random.randrange(1, maxSize)
    value = random.randrange(1, maxValue)
    print(size, value)
