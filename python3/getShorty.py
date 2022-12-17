# import min-heap operations 
from heapq import heappush, heappop

# graph: a list of lists of tuples [ [ (edgeCost, w), ...], ...]
# start: starting vertex as key to graph
# Output: the shortest distance to all vertices from start vertex
def Dijkstra(graph, start):
    distance = [None] * len(graph)
    queue = [(-1, start)]
    while len(queue) != 0:
        pathCost, v = heappop(queue)
        if distance[v] is None:
            distance[v] = pathCost
            for edgeCost, w in graph[v]:
                if distance[w] is None:
                    heappush(queue, (pathCost * edgeCost, w))
    return distance

def main():
    params = input().split()
    params = [int(x) for x in params]
    while not (params[0] == 0 and params[1] == 0):
        graph = []
        for i in range(params[0]):
            graph.append([])
        for i in range(params[1]):
            edge = input().split()
            graph[int(edge[0])].append( (float(edge[2]), int(edge[1])) )
            graph[int(edge[1])].append( (float(edge[2]), int(edge[0])) )
        result = Dijkstra(graph, 0)
        scale = str( round(0 - result[-1],4) )
        if '.' not in scale:
            scale += '.'
        scale += '0'*(4-len(scale.split('.')[1]))
        print(scale)

        params = input().split()
        params = [int(x) for x in params]
main()