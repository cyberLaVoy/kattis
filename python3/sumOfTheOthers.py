import sys

nums = sys.stdin.readline()
while nums != '':
    nums = nums.strip().split()
    nums = [int(x) for x in nums]
    for i in range(len(nums)):
        exclude = nums[i]
        total = sum(nums[:i] + nums[i+1:])
        if total == exclude:
            print(exclude)
            break
    nums = sys.stdin.readline()