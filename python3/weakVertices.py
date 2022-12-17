

def findWeakVertices(graph, sizeV):
    weakVertices = []
    for i in range(sizeV):
        isWeak = True
        for j in range(sizeV):
            if i == j:
                continue
            for k in range(sizeV):
                if i == k or j == k:
                    continue
                if graph[i][k] and graph[i][j] and graph[j][k]:
                        isWeak = False
        if isWeak:
            weakVertices.append(i)
    return weakVertices



def main():
    sizeV = int(input())
    while sizeV != -1:
        graph = []
        for _ in range(sizeV):
            graph.append([int(x) for x in input().split()])
        weakVertices = findWeakVertices(graph, sizeV)
        sizeV = int(input())
        print(" ".join(str(x) for x in weakVertices))

main()