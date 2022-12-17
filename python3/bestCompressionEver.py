
params = input().split()

numsFiles = int(params[0])
compression = int(params[1])

compressed = (1 << (compression+1)) - 1 
if compressed >= numsFiles:
    print("yes")
else:
    print("no")
