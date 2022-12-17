import math

nums = input().split()
nums = [float(x) for x in nums]
while not (nums[0] == 0 and nums[1] == 0 and nums[2] == 0):
    radius = nums[0]
    totalMarked = nums[1]
    markedInCircle = nums[2]
    print(math.pi*radius**2, (2*radius)**2*markedInCircle/totalMarked)
    nums = input().split()
    nums = [float(x) for x in nums]