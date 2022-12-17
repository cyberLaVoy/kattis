

def pickUp(bank, ferryLimit, ferrySide):
    pickUpSize = 0
    cars = []
    while len(bank) != 0:
        if bank[len(bank)-1]["size"] <= ferryLimit:
            pickUpSize += bank[len(bank)-1]["size"]
            if pickUpSize <= ferryLimit:
                cars.append(bank.pop())
            else:
                return cars
    return cars
            

def numTrips(leftBank, rightBank, ferrySize):
    leftBank.reverse()
    rightBank.reverse()
    ferrySide = "left"
    numTrips = 0
    while len(leftBank) != 0 or len(rightBank) != 0:
        if ferrySide == "left" and len(leftBank) != 0:
            cars = pickUp(leftBank, ferrySize, ferrySide)
            numTrips += 1
            ferrySide = "right"
        elif ferrySide == "right" and len(rightBank) != 0:
            cars = pickUp(rightBank, ferrySize, ferrySide)
            numTrips += 1
            ferrySide = "left"
        elif ferrySide == "left" and len(rightBank) != 0:
            numTrips += 1
            cars = pickUp(rightBank, ferrySize, ferrySide)
            numTrips += 1
        elif ferrySide == "right" and len(leftBank) != 0:
            numTrips += 1
            cars = pickUp(leftBank, ferrySize, ferrySide)
            numTrips += 1
    return numTrips
        
def solve():
    numTests = int(input())
    for i in range(numTests):
        parameters = input().split()
        ferrySize = 100*int(parameters[0])
        numCars = int(parameters[1])
        leftBank = []
        rightBank = []
        for j in range(numCars):
            car = input().split()
            car = {"size": int(car[0]), "side": car[1]}
            if car["side"] == "left":
                leftBank.append(car)
            else:
                rightBank.append(car)
        print(numTrips(leftBank,rightBank, ferrySize))
solve()