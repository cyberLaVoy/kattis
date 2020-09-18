

def firstNonZeroDigitIndex(value):
    value = str(value)
    j = 0
    for i in range(len(value)-1,-1,-1):
        if value[i] != '0':
            return j
        j += 1

numTests = int(input())

for i in range(numTests):
    value = int(input())
    j = firstNonZeroDigitIndex(value)
    value -= 10**j
    print(value)