import sys

translation = {'***  *****  ***': 2, '* ** ****  *  *': 4, '**** ***** ****': 8, '***  ****  ****': 3, '**** ****  ****': 9, '**** ** ** ****': 0, '****  **** ****':
6, '***  *  *  *  *': 7, '****  ***  ****': 5, '  *  *  *  *  *': 1}

def createEncodingArr(lineSize):
    numEncodedDigits = int(1 + (lineSize-3)/4)
    encodingArr = [""]*numEncodedDigits
    return encodingArr

def parseInput():
    arrCreated = False
    for line in sys.stdin:
        if not arrCreated:
            lineSize = len(line)
            encodingArr = createEncodingArr(lineSize)
            arrCreated = True
        partialString = ""
        start = 0
        end = 3
        for i in range(len(encodingArr)):
            for j in range(start, end):
                partialString += line[j]
            encodingArr[i] += partialString
            partialString = ""
            start = end + 1
            end += 4

    return encodingArr

def parseEncoding(encodingArr):
    value = 0
    placeValue = 1
    for i in range(len(encodingArr)-1,-1,-1):
        if encodingArr[i] in translation:
            value += translation[encodingArr[i]]*placeValue
            placeValue *= 10
        else:
            return None
    return value

def testValue(value):
    if value % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")

def main():
    encodingArr = parseInput()
    translatedValue = parseEncoding(encodingArr)
    if translatedValue is None:
        print("BOOM!!")
    else:
        testValue(translatedValue)
main()
        
            

