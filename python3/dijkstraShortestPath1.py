from queue import PriorityQueue

def dijkstra(graph, start):
    d = [None]*len(graph)
    q = PriorityQueue()
    q.put( (0, start) )
    while not q.empty():
        pathCost, u = q.get()
        if d[u] is None:
            d[u] = pathCost
            for edgeCost, v in graph[u]: 
                if d[v] is None:
                    q.put( (pathCost+edgeCost, v) )
    return d

def makeGraph(n, m):
    graph = []
    for _ in range(n):
        graph.append([])
    for _ in range(m):
        edge = [int(x) for x in input().split()]
        graph[edge[0]].append( (edge[2], edge[1]) )
    return graph

def main():
    while True:
        n, m, q, s = [int(x) for x in input().split()]
        if n == 0 and m == 0 and q == 0 and s == 0:
            break
        graph = makeGraph(n, m)
        dists = dijkstra(graph, s)
        for _ in range(q):
            a = dists[int(input())]
            if a is None:
                print("Impossible")
            else:
                print(a)
        print()
main()






