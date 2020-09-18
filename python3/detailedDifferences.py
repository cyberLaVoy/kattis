
numTests = int(input())

for i in range(numTests):
    string1 = input()
    string2 = input()
    print(string1)
    print(string2)
    compareString = ""
    for j in range(len(string1)):
        if string1[j] == string2[j]:
            compareString += '.'
        else:
            compareString += '*'
    print(compareString)
