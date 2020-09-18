
def solve():
    input() # ignore first param
    nums = input().split()
    nums = [int(x) for x in nums]

    # big-O n
    leftCandidates = {}
    largestFound = nums[0]
    leftCandidates[largestFound] = "Possible."
    for i in range(1, len(nums)):
        if nums[i] > largestFound:
            largestFound = nums[i]
            leftCandidates[largestFound] = "Possible."

    # big-O n
    rightCandidates = {}
    smallestFound = nums[-1]
    rightCandidates[smallestFound] = "Possible."
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < smallestFound:
            smallestFound = nums[i]
            rightCandidates[smallestFound] = "Possible."

    # big-O n
    pivots = [] 
    for candidate in leftCandidates:
        if candidate in rightCandidates: 
            pivots.append(candidate)

    # big-O n
    totalPivots = len(pivots)
    print(totalPivots)

solve()
