import sys

nums = sys.stdin.readline()
case = 1
while nums != '':
    nums = nums.strip().split()
    nums = [int(x) for x in nums]
    nums = nums[1:]
    minimum = min(nums)
    maximum = max(nums)
    print("Case " + str(case) + ':', minimum, maximum, maximum-minimum)
    case += 1
    nums = sys.stdin.readline()