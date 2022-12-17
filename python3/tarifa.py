
maxMB = int(input())
numMonths = int(input())

MBavailable = 0
for i in range(numMonths):
    MBavailable += maxMB
    MBspent = int(input())
    MBavailable -= MBspent

MBavailable += maxMB
print(MBavailable)

