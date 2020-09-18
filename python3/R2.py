import sys

integers = sys.stdin.readline().strip().split(' ')
R1 = int(integers[0])
S = int(integers[1])

R2 = 2*S-R1
print(R2)

