
dimensions = input().split()

dimensions = [int(x) for x in dimensions]

dimensions.sort()

print(dimensions[0]*dimensions[2])