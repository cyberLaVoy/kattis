
def passChecksum(digits):
    for i in range(len(digits)-2,-1,-2):
        digits[i] *= 2
        stringVersion = str(digits[i])
        if len(stringVersion) == 2:
            digits[i] = int(stringVersion[0]) + int(stringVersion[1])
    if sum(digits) % 10 == 0:
        return True
    return False

def solve():
    numTests = int(input())

    for i in range(numTests):
        nums = input()
        nums = [int(x) for x in nums]
        if passChecksum(nums):
            print("PASS")
        else:
            print("FAIL")
solve()