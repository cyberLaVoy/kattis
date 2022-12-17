
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def gcdList(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd(result, nums[i])
    return result


def main():
    numTests = int(input())
    for test in range(numTests):
        input() # discard nums count
        nums = [int(x) for x in input().split()]
        magicalGCD = 1
        for i in range(1, len(nums)+1):
            candidate = gcdList(nums[:i])*i
            if candidate > magicalGCD:
                magicalGCD = candidate
        for i in range(len(nums)-1, -1, -1):
            candidate = gcdList(nums[i:])*(len(nums)-i)
            if candidate > magicalGCD:
                magicalGCD = candidate
    print(magicalGCD)
                


if __name__ == "__main__":
    main()