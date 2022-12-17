import sys

nums = sys.stdin.readline().strip()
while nums != '':
    nums = nums.split()
    diffence = abs(int(nums[0]) - int(nums[1]))
    print(diffence)
    nums = sys.stdin.readline().strip()