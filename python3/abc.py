
nums = input().split()
nums = [int(x) for x in nums]
nums.sort()
lookup = {'A':nums[0], 'B':nums[1], 'C':nums[2]}

order = input()
for l in order:
    print(lookup[l], end=' ')
print()