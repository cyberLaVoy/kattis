import math

nums = input().split()
nums = [int(x) for x in nums]
while not (nums[0] == 0 and nums[1] == 0):
    numer = nums[0]
    denom = nums[1]
    whole = math.floor(numer/denom)
    newNumer = numer%denom
    print(whole, newNumer, '/', denom)
    nums = input().split()
    nums = [int(x) for x in nums]

