import sys


class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0

# with path compression
def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

# union by rank
def union(x, y):
    xRoot = find(x)
    yRoot = find(y)
    # x and y are already in the same set
    if xRoot == yRoot:
        return
    # x and y are not in same set, so we merge them
    if xRoot.rank < yRoot.rank:
        xRoot, yRoot = yRoot, xRoot # swap xRoot and yRoot
    # merge yRoot into xRoot
    yRoot.parent = xRoot
    if xRoot.rank == yRoot.rank:
        xRoot.rank += 1

def solve():
    lines = sys.stdin.readlines()
    linesIndex = 0

    params = lines[linesIndex].strip().split()
    linesIndex += 1

    numItems = int(params[0])
    nodes = []
    for i in range(numItems):
        nodes.append(Node())

    numOperations = int(params[1])
    for i in range(numOperations):
        operation = lines[linesIndex].strip().split()
        linesIndex += 1
        action = operation[0]
        a = int(operation[1])
        b = int(operation[2])

        if action == '=': # union
            union(nodes[a], nodes[b])
        else: # find
            if find(nodes[a]) == find(nodes[b]):
                print("yes")
            else:
                print("no")

solve()
