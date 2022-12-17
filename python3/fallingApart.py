
input()

nums = input().split()
nums = [int(x) for x in nums]
nums.sort()

alice = 0
bob = 0
turn = 0
while len(nums) != 0:
    if turn & 1 == 1:
        bob += nums.pop()
    else:
        alice += nums.pop()
    turn += 1

print(alice, bob)

