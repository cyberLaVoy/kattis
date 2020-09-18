
nums = []
for i in range(int(input())):
    nums.append(int(input()))

recited = [False]*(max(nums)+1)

for v in nums:
    recited[v] = True

missing = False
for i in range(1, len(recited)):
    if not recited[i]:
        print(i)
        missing = True

if not missing:
    print("good job")


