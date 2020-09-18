
amounts = input().split()
amounts = [int(x) for x in amounts]

ratio = input().split()
ratio = [int(x) for x in ratio]

quantities = [amounts[i]/ratio[i] for i in range(len(amounts))]

minQuantity = min(quantities)
leftOver = [amounts[i]-minQuantity*ratio[i] for i in range(len(quantities))]
for v in leftOver:
    print(v, end=' ')
print()
