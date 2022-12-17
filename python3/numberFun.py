

numTests = int(input())

for i in range(numTests):
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    possible = False
    if a-b == c or b-a == c:
        possible = True
    elif a+b == c or b+a == c:
        possible = True
    elif a*b == c or b*a == c:
        possible = True
    elif a/b == c or b/a == c:
        possible = True
    if possible:
        print("Possible")
    else:
        print("Impossible")

