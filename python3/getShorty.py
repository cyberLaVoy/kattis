from heapq import heappush, heappop

def Dijkstra(graph, start):
    dist = [None] * len(graph)
    queue = [(-1, start)]
    while len(queue) != 0:
        pathCost, v = heappop(queue)
        if dist[v] is None: # v is unvisited
            dist[v] = pathCost
            for w, edgeCost in graph[v].items():
                if dist[w] is None: # w is unvisited
                    heappush(queue, (pathCost * edgeCost, w))
    return dist


def main():
    params = input().split()
    params = [int(x) for x in params]
    while not (params[0] == 0 and params[1] == 0):
        graph = {}
        for i in range(params[0]):
            graph[i] = {}
        for i in range(params[1]):
            edge = input().split()
            graph[int(edge[0])][int(edge[1])] = float(edge[2])
            graph[int(edge[1])][int(edge[0])] = float(edge[2])
        result = Dijkstra(graph, 0)
        scale = str( round(0 - result[-1],4) )
        if '.' not in scale:
            scale += '.'
        scale += '0'*(4-len(scale.split('.')[1]))
        print(scale)

        params = input().split()
        params = [int(x) for x in params]
main()