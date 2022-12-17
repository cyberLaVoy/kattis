import math

params = input().split()

bobAge = int(params[0])
bobRetireAge = int(params[1])
bobAmount = int(params[2])
aliceAge = int(params[3])
aliceAmount = int(params[4])

bobYears = bobRetireAge - bobAge
bobSavings = bobYears*bobAmount

aliceRetireAge = math.ceil(bobSavings/aliceAmount+aliceAge)
aliceYears = aliceRetireAge - aliceAge
aliceSavings = aliceYears*aliceAmount
if aliceSavings > bobSavings:
    print(aliceRetireAge)
else:
    print(aliceRetireAge+1)


