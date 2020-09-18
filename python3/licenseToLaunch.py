
input() # throw away n
spaceJunk = input().split()
spaceJunk = [int(x) for x in spaceJunk]

leastJunk = min(spaceJunk)
for i in range(len(spaceJunk)):
    if spaceJunk[i] == leastJunk:
        print(i)
        break