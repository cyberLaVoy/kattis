fibonacciNumbers = {1: 2, 2: 3, 3: 4, 5: 5, 8: 6, 2504730781961: 61, 13: 7, 75025: 25, 21: 8, 2584: 18, 701408733: 44, 2178309: 32, 46368: 24, 7778742049: 49, 34: 9, 121393: 26, 832040: 30, 39088169: 38, 679891637638612258: 87, 17711: 22, 806515533049393: 73, 55: 10, 267914296: 42, 956722026041: 59, 1597: 17, 1134903170: 45, 4807526976: 48, 117669030460994: 69, 61305790721611591: 82, 86267571272: 54, 72723460248141: 68, 3416454622906707: 76, 4181: 19, 27777890035288: 66, 89: 11, 1836311903: 46, 498454011879264: 72, 12586269025: 50, 37889062373143906: 81, 53316291173: 53, 6557470319842: 63, 8944394323791464: 78, 6765: 20, 317811: 28, 377: 14, 14472334024676221: 79, 5527939700884757: 77, 20365011074: 51, 420196140727489673: 86, 196418: 27, 190392490709135: 70, 144: 12, 1304969544928657: 74, 610: 15, 591286729879: 58, 259695496911122585: 85, 17167680177565: 65, 2111485077978050: 75, 365435296162: 57, 433494437: 43, 99194853094755497: 83, 1100087778366101931: 88, 139583862445: 55, 14930352: 36, 514229: 29, 165580141: 41, 10610209857723: 64, 225851433717: 56, 10946: 21, 9227465: 35, 102334155: 40, 63245986: 39, 1548008755920: 60, 308061521170129: 71, 24157817: 37, 4052739537881: 62, 987: 16, 1346269: 31, 2971215073: 47, 3524578: 33, 32951280099: 52, 23416728348467685: 80, 5702887: 34, 233: 13, 160500643816367088: 84, 28657: 23, 44945570212853: 67}

def explore(graph, v, visited, ccnum, cc, pre, post, clock):
    visited[v] = True
    # previsit
    ccnum[v] = cc
    pre[v] = clock[0]
    clock[0] += 1
    for u in graph[v]:
        if not visited[u]:
            explore(graph, u, visited, ccnum, cc, pre, post, clock)
    # postvisit
    post[v] = clock[0]
    clock[0] += 1

# graph: a list of lists (adjacency list) [ [ w0, w1, ...], ...]
def dfs(graph):
    visited = [False]*len(graph)
    ccnum = [-1]*len(graph)
    pre = [-1]*len(graph)
    post = [-1]*len(graph)
    cc = 0
    clock = [1]
    for v in range(len(graph)):
        if not visited[v]:
            cc += 1
            explore(graph, v, visited, ccnum, cc, pre, post, clock)
    return ccnum, pre, post

def countMaxUnique(values):
    uniqueCounts = [0]*(max(values)+1)
    for v in values:
        uniqueCounts[v] += 1
    maxCount = max(uniqueCounts)
    return maxCount, uniqueCounts.index(maxCount)

def edgeCases(mansionSizes, numMansions):
    excludes = []
    for i in range(len(mansionSizes)):
        if mansionSizes[i] not in fibonacciNumbers:
            excludes.append(i)

    # edge cases
    if len(excludes) == numMansions:
        print(0)
        return True
    if len(excludes) == numMansions - 1:
        print(1)
        return True
    return False

def tours(ccnum, mansionSizes, connectedOnes):
    tours = []
    for i in range(max(ccnum)+1):
        tours.append([])
    for i in range(len(ccnum)):
        tours[ccnum[i]].append(mansionSizes[i])
    tours = [list(set(x)) for x in tours]
    for tour in tours:
        if connectedOnes and 1 in tour:
            tour.append(1)
    return tours

def getLongestTour(tours):
    lengths = [len(tour) for tour in tours]
    return list(tours[lengths.index(max(lengths))])


def main():
    dim = input().split()
    numMansions, numRoads = int(dim[0]), int(dim[1])
    mansionSizes = [int(x) for x in input().split()]
    if edgeCases(mansionSizes, numMansions):
        return
    connectedOnes = False
    graph = []
    for i in range(numMansions):
        graph.append([])
    for i in range(numRoads):
        road = [int(x)-1 for x in input().split()]
        bothIncluded = mansionSizes[road[0]] in fibonacciNumbers and mansionSizes[road[1]] in fibonacciNumbers
        if bothIncluded:
            adjecent = abs(fibonacciNumbers[mansionSizes[road[0]]]-fibonacciNumbers[mansionSizes[road[1]]]) == 1
            default = mansionSizes[road[0]] == 1 and mansionSizes[road[1]] == 1
            if default:
                connectedOnes = True
            if adjecent or default:
                graph[road[0]].append(road[1])
                graph[road[1]].append(road[0])
    ccnum, _, _ = dfs(graph)
    allTours = tours(ccnum, mansionSizes, connectedOnes)
    longestTour = getLongestTour(allTours)
    print(len(longestTour))


if __name__ == "__main__":
    main()