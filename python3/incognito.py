
numTests = int(input())

for i in range(numTests):
    numItems = int(input())
    items = {}
    for j in range(numItems):
        item = input().split()
        category = item[1]
        name = item[0]
        if category not in items:
            items[category] = []
        items[category].append(name)
    combos = 1
    for cat in items:
        combos *= (len(items[cat])+1) # wearing any one item from category, or none
    print(combos-1) # take away the case where no disguise is used