
numTestCases = int(input())

for i in range(numTestCases):
    cities = {}
    numCities = int(input())
    for j in range(numCities):
        city = input()
        cities[city] = 1
    print(len(cities))