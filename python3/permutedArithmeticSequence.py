
def isArithmetic(nums):
    difference = nums[1] - nums[0]
    for i in range(len(nums)-1):
        if nums[i+1] != nums[i] + difference:
            return False
    return True

def solve():
    numTests = int(input())

    for i in range(numTests):
        nums = input().split()[1:]
        nums = [int(x) for x in nums]
        if isArithmetic(nums):
            print("arithmetic")
        else:
            nums.sort() 
            if isArithmetic(nums):
                print("permuted arithmetic")
            else:
                print("non-arithmetic")
solve()
