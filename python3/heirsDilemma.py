
def divisibleByAllDigits(num):
    strNum = str(num)
    for i in range(len(strNum)):
        if num%int(strNum[i]) != 0:
            return False
    return True
def allUniqueDigits(num):
    strNum = str(num)
    unique = {}
    for i in range(len(strNum)):
        if strNum[i] in unique:
            return False
        unique[strNum[i]] = "found"
    return True

fullRange = input().split()
start = int(fullRange[0])
end = int(fullRange[1])

possibleCount = 0
for i in range(start, end+1):
    if '0' not in str(i) and divisibleByAllDigits(i) and allUniqueDigits(i):
        possibleCount += 1
print(possibleCount)
