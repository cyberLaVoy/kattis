def updateDogs(dogs, time):
    for dog in dogs:
        frame = dogs[dog]["aTime"]+dogs[dog]["rTime"]
        interval = time % (frame)
        if interval == 0:
            interval = frame 
        if interval > dogs[dog]["aTime"]:
            dogs[dog]["agressive"] = False
        else:
            dogs[dog]["agressive"] = True

def solve():
    dogsParams = input().split()
    personTimes = input().split()
    personTimes = [int(x) for x in personTimes]
    dog1 = {"agressive":True , "aTime": int(dogsParams[0]),"rTime": int(dogsParams[1])} 
    dog2 = {"agressive":True , "aTime": int(dogsParams[2]),"rTime": int(dogsParams[3])}
    dogs = {1: dog1, 2: dog2}

    for i in range(len(personTimes)):
        arrival = personTimes[i]
        updateDogs(dogs, arrival)
        numAttacks = 0
        for dog in dogs:
            if dogs[dog]["agressive"]:
                numAttacks += 1
        if numAttacks == 0:
            print("none")
        elif numAttacks == 1:
            print("one")
        else:
            print("both")

solve()
