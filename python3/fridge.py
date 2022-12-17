

def getDigitCounts(digits):
    digitCounts = [0]*10
    for digit in digits:
        digitCounts[int(digit)] += 1
    return digitCounts
def getLowestCountedDigits(digitCounts):
    lowestCount = min(digitCounts)
    lowestCountedDigits = []
    for i in range(len(digitCounts)):
        if digitCounts[i] == lowestCount:
            lowestCountedDigits.append((i,digitCounts[i]))
    return lowestCountedDigits
def smallestIntegerNotPossible(lowestCountedDigits):
    if lowestCountedDigits[0][0] == 0 and len(lowestCountedDigits) == 1:
        return 10**(lowestCountedDigits[0][1]+1) 
    elif lowestCountedDigits[0][0] == 0:
        return str(lowestCountedDigits[1][0])*(lowestCountedDigits[1][1]+1)
    else:
        return str(lowestCountedDigits[0][0])*(lowestCountedDigits[0][1]+1)

def solve():
    digits = input()
    digitCounts = getDigitCounts(digits)
    lowestCountedDigits = getLowestCountedDigits(digitCounts)
    answer = smallestIntegerNotPossible(lowestCountedDigits)
    print(answer)
solve()



