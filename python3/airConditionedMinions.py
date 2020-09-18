

def highTemp(element):
    return element["high"]
def getTempPref(numMinions):
    tempPref = []
    for i in range(numMinions):
        prefRange = input().split()
        low = int(prefRange[0])
        high = int(prefRange[1])
        prefDetails = {"low" : low, "high" : high}
        tempPref.append(prefDetails)
    tempPref.sort(key=highTemp)
    return tempPref
def determineNumRooms(tempPref):
    numRooms = 1
    threshold = tempPref[0]["high"]
    for i in range(1, len(tempPref)):
        if tempPref[i]["low"] > threshold:
            numRooms += 1
            threshold = tempPref[i]["high"]
    return numRooms
def solve():
    numMinions = int(input())
    tempPref = getTempPref(numMinions)
    numRooms = determineNumRooms(tempPref)
    print(numRooms)
solve()