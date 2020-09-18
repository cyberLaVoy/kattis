
uniqueTracker = {}

for i in range(10):
    num = int(input())
    uniqueTracker[num%42] = "unique!" 
print(len(uniqueTracker))
