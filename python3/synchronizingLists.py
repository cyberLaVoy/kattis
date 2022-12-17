
def gatherList(listLength):
    newList = []
    for i in range(listLength):
        newList.append(int(input()))
    return newList

def getSyncronization(syncedList):
    ordered = syncedList[:]
    ordered.sort()
    syncedIndexes = []
    for v in ordered:
        for i in range(len(syncedList)):
            if v == syncedList[i]:
                syncedIndexes.append(i)
                break
    return syncedIndexes

def syncronize(unsynced, syncedIndexes):
    ordered = unsynced[:]
    ordered.sort()
    for i in range(len(ordered)):
        unsynced[syncedIndexes[i]] = ordered[i]
    

def solve():
    listLength = int(input())
    while listLength != 0:
        synced = gatherList(listLength)
        syncedIndexes = getSyncronization(synced)
        unsynced = gatherList(listLength)
        syncronize(unsynced, syncedIndexes)
        for v in unsynced:
            print(v)
        print()
        listLength = int(input())
solve()