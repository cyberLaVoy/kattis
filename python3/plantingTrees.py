
numSeedlings = int(input())

seedlings = input().split()
seedlings = [int(x) for x in seedlings] # big-O n
# big-O nlogn
seedlings.sort() # to plant the seedlings that will take the longest first
growing = []
days = 0
longest = 0
countDown = numSeedlings-1 # number of days a particular seedling will have to grow, after planting all
while len(growing) != numSeedlings: # big-O n
    seedling = seedlings.pop()-countDown
    growing.append(seedling)
    if seedling > longest:
        longest = seedling
    countDown -= 1 # seedlings will have less time to grow as the rest are planted
    days += 1
days += longest # number of days left for last seedling to grow
print(days+1)
