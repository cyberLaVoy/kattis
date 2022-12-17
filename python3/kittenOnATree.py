from queue import Queue

# graph: a list of lists (adjacency list) [ [ w0, w1, ...], ...]
# start: starting vertex as index to adjacency list
# Output: the step-wise distance to all vertices from start vertex
def bfs(graph, start):
    distance = [None]*len(graph)
    distance[start] = 0
    queue = Queue() # FIFO queue
    queue.put(start)
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if distance[v] is None:
                queue.put(v)
                distance[v] = distance[u] + 1
    return distance

def dist(obj):
    return obj[0]

def main():
    start = int(input())
    branching = [int(x) for x in input().split()]
    graph = []
    for i in range(101):
        graph.append([])
    while branching[0] != -1:
        for i in range(1, len(branching)):
            graph[branching[i]].append(branching[0])
        branching = [int(x) for x in input().split()]
    distance = bfs(graph, start)
    path = []
    for i in range(len(distance)):
        if distance[i] is not None:
            path.append((distance[i], i))
    path.sort(key=dist)
    print(" ".join(str(x[1]) for x in path))



if __name__ == "__main__":
    main()