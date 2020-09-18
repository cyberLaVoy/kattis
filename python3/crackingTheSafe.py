from queue import Queue

def unrotate(value):
    return (value-1)%4
def rotate(value):
    return (value+1)%4

def unpush(config, i , j): 
    config[i][j] = rotate(config[i][j])
    config[i] = [unrotate(x) for x in config[i]]
    for k in range(len(config)):
        config[k][j] = unrotate(config[k][j])
    return config

def unravel(config):
    config = [int(x) for x in config]
    return [config[:3], config[3:6], config[6:]]

def ravel(config):
    raveled = ""
    for i in range(len(config)):
        for j in range(len(config[i])):
           raveled += str(config[i][j])
    return raveled

def getBranhces(config):
    config = unravel(config)
    branches = []
    temp = [l[:] for l in config]
    for i in range(len(config)):
        for j in range(len(config[i])):
            branch = unpush(temp, i , j)
            branches.append(ravel(branch))
            temp = [l[:] for l in config]
    return branches


def genActionTree():
    q = Queue()
    start = "000000000"
    distance = {}
    visited = {}
    visited[start] = True
    distance[start] = 0
    q.put(start)
    while not q.empty():
        u = q.get()
        for v in getBranhces(u):
            if v not in visited:
                visited[v] = True
                distance[v] = distance[u]+1
                q.put(v)
    return distance


def main():
    moves = genActionTree()
    config = []
    for i in range(3):
        config.append(input().split())
    config = ravel(config)
    if config not in moves: 
        print(-1)
    else:
        print(moves[config])

if __name__ == "__main__":
    main()