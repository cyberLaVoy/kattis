

def numCarsSquashed(section):
    numCars = 0
    for char in section:
        if char == 'X':
            numCars += 1
    return numCars

dimensions = input().split()
numRows = int(dimensions[0])
numCols = int(dimensions[1])

layout = []
for i in range(numRows):
    row = input()
    layout.append(row)

parking = {0:0, 1:0, 2:0, 3:0, 4:0}
for i in range(numRows-1):
    for j in range(numCols-1):
        section = layout[i][j] + layout[i][j+1] + layout[i+1][j] + layout[i+1][j+1]
        if '#' not in section:
            numCars = numCarsSquashed(section)
            parking[numCars] += 1

for carsSquashed in parking:
    print(parking[carsSquashed])
