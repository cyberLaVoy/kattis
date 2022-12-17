
numContestants = int(input())

categories = {}
for i in range(numContestants):
    category = input()
    if category in categories:
        categories[category] += 1
    else:
        categories[category] = 1

minNumInCat = min(categories.values())
bestChance = []
for category in categories:
    if categories[category] == minNumInCat:
        bestChance.append(category)

bestChance.sort()
for cat in bestChance:
    print(cat)