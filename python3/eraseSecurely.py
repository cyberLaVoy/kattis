
def flipped(string):
    newString = ""
    for l in string:
        if l == '0':
            newString += '1'
        else:
            newString += '0'
    return newString

numAnds = int(input())

original = input()
goal = input()

if numAnds & 1 != 1 and original == goal:
        print("Deletion succeeded")
elif numAnds & 1 == 1 and flipped(original) == goal:
        print("Deletion succeeded")
else:
    print("Deletion failed")

