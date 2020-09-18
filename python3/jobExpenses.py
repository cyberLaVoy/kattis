
input() #discard N

nums = [int(x) for x in input().split()]

total = 0
for v in nums:
    if v < 0:
        total += v
print(abs(total))