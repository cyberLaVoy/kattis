

def cupRadius(cup):
    return cup[1]

numCups = int(input())

cups = []
for i in range(numCups):
    cup = input().split()
    if cup[0].isdigit():
        cups.append((cup[1],int(int(cup[0])/2)))
    else:
        cups.append((cup[0],int(cup[1])))

cups.sort(key=cupRadius)
for cup in cups:
    print(cup[0])
