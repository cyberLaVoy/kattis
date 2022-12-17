import math

n = int(input())

estimate = 0
denominator = 1
for i in range(0, n+1):
    estimate += (1/denominator)
    denominator *= (i+1)
print(estimate)

