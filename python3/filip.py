import sys

def extractPlaceValue(value, place):
    value %= (place*10)    # remove leading digits
    value -= (value%place) # subtract away everything but the place value
    value //= place        # leave only the desired digit   
    return value

def flipNumber(value):
    flippedValue = 0
    placeValues = []
    place = 1
    while (value % place) != value: 
        placeValues.append(extractPlaceValue(value, place))
        place *= 10
    place //= 10
    for value in placeValues:
        flippedValue += value*place
        place //= 10
    return flippedValue

def printLargestValue(value1, value2):
    if value1 > value2:
        print(value1)
    else:
        print(value2)

def main():
    values = sys.stdin.readline().strip().split(' ')
    value1 = int(values[0])
    value2 = int(values[1])
    flippedValue1 = flipNumber(value1)
    flippedValue2 = flipNumber(value2)
    printLargestValue(flippedValue1, flippedValue2)
main()
