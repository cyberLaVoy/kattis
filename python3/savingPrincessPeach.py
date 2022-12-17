
params = input().split()

totalObsacles = int(params[0])
numFound = int(params[1])

found = [False]*totalObsacles
for i in range(numFound):
    found[int(input())] = True

totalFound = 0
for i in range(len(found)):
    if not found[i]:
        print(i)
    else:
        totalFound += 1
print("Mario got", totalFound ,"of the dangerous obstacles.")
