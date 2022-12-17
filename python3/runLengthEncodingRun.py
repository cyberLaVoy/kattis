def encode(message):
    newMessage = ""
    i = 0
    while i < len(message):
        letter = message[i]
        newMessage += letter
        letterCount = 0
        while message[i] == letter:
            letterCount += 1
            i += 1
            if i >= len(message):
                break
        newMessage += str(letterCount)
    print(newMessage)

def decode(message):
    newMessage = ""
    i = 0
    while i < len(message)-1:
        letter = message[i]
        newMessage += letter*int(message[i+1])
        i += 2
    print(newMessage)

def solve():
    params = input().split()
    eOrD = params[0]
    message = params[1]
    if eOrD == 'E':
        encode(message)
    else:
        decode(message)
solve()


