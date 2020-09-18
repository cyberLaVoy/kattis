
def solve():
    numTests = int(input())

    for i in range(numTests):
        phoneNumbers = {}
        phoneNumbersCount = int(input())
        isConsistent = True
        for j in range(phoneNumbersCount):
            phoneNumber = input()
            phoneNumbers[phoneNumber] = phoneNumber
        for phoneNumber in phoneNumbers:
            for k in range(1, len(phoneNumber)+1):
                prefix = phoneNumber[0:k]
                if prefix in phoneNumbers and phoneNumbers[phoneNumber] != prefix:
                    isConsistent = False
        if isConsistent:
            print("YES")
        else:
            print("NO")

solve()
