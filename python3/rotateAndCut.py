

def rotateAndCut(message, numRepeats):
    leftCuts = 0
    rightCuts = 0
    cutSize = int(len(message)*.25)
    remainder = len(message) - cutSize
    for i in range(numRepeats):
        if cutSize == 0:
            break
        if i & 1 == 0:
            leftCuts += cutSize
        else:
            rightCuts += cutSize
        cutSize = int(remainder*.25)
        remainder = remainder - cutSize
    return message[leftCuts:len(message)-rightCuts]



def main():
    numTests = int(input())
    for _ in range(numTests):
        params = input().split()
        numRepeats = int(params[0])
        message = params[1]
        print(rotateAndCut(message, numRepeats))

main()