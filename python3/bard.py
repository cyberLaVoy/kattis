

def learnFromBard(villagers, present, song):
    for person in present: 
        villagers[person].append(song)
        villagers[person] = list(set(villagers[person]))
def learnFromEachother(villagers, present):
    learningPool = []
    for person in present:
        learningPool += villagers[person]
    learningPool = list(set(learningPool))
    for person in present:
        villagers[person] = learningPool[:]


def solve():
    numVillagers = int(input())
    numNights = int(input())

    villagers = {}
    keys = []
    for i in range(1, numVillagers+1):
        villagers[i] = []
        keys.append(i)

    for i in range(numNights):
        present = input().split()[1:]
        present = [int(x) for x in present]
        if 1 in present: 
            learnFromBard(villagers, present, i)
        else:
            learnFromEachother(villagers, present)
    for person in keys:
        if len(villagers[person]) == len(villagers[1]):
            print(person)
solve()
