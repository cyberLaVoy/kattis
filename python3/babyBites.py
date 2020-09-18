
numBites = int(input())
counting = input().split()

fishy = False
for i in range(1, numBites+1):
    if counting[i-1] != str(i) and counting[i-1] != "mumble":
        fishy = True
        break
if fishy:
    print("something is fishy")
else:
    print("makes sense")

    