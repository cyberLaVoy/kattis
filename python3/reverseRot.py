
translation = {}
letters = "ABCDEFGHIJKLMPNOQRSTUVWXYZ"
for l in letters:
    translation[l] = ord(l) - 65
translation['_'] = 26
translation['.'] = 27

reverseTranslation = {}
for l in translation:
    reverseTranslation[translation[l]] = l

testCase = input().split()
testCase[0] = int(testCase[0])
while testCase[0] != 0:
    rotation = testCase[0]
    message = testCase[1]
    message = [translation[message[i]] for i in range(len(message)-1,-1,-1)] # reverse and translate to ascii
    for i in range(len(message)):
        message[i] = (message[i] + rotation) % len(translation)
    newMessage = ""
    for i in range(len(message)):
        newMessage += reverseTranslation[message[i]]
    print(newMessage)

    testCase = input().split()
    testCase[0] = int(testCase[0])
