

def fillDigitDict(dict, value):
    for digit in value:
        dict[digit] = 0
    for digit in value:
        dict[digit] += 1

def solve():
    value = input()
    numDigits = len(value)
    maxValue = 10**numDigits

    containsDigits = {}
    fillDigitDict(containsDigits, value)

    matchFound = False
    for i in range(int(value)+1, maxValue):
        possibleMatch = str(i)
        tempContainsDigits = {}
        fillDigitDict(tempContainsDigits, possibleMatch) 
        match = True
        for key in tempContainsDigits:
            if key not in containsDigits or containsDigits[key] != tempContainsDigits[key]:
                match = False 
                break
        if match:
            matchFound = True
            print(i)
            break
    if not matchFound:
        print(0)
solve()