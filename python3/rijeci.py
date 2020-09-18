
pressed = int(input())

numAs = 1
numBs = 0
for i in range(pressed):
    tempNumBs = numBs + numAs
    numAs += numBs-numAs
    numBs = tempNumBs
print(numAs, numBs)