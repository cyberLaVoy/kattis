
def solve():
    nums = input().split()
    nums = [int(x) for x in nums]
    nums.sort()

    minRange = min(nums[1]-nums[0], nums[2]-nums[1])
    if minRange == 0:
        print(nums[0])
        return

    sequence = [nums[0]]
    for i in range(4):
        sequence.append(sequence[i]+minRange)

    for v in sequence:
        if v not in nums:
            print(v)
            return
solve()