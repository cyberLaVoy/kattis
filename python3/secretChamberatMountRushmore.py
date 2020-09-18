from queue import Queue

def isPath(v1, v2, graph):
    visited = [False]*len(graph)
    distance = [None]*len(graph)
    distance[v1] = 0
    visited[v1] = True
    q = Queue()
    q.put(v1)
    while not q.empty():
        u = q.get()
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                q.put(v)
                distance[v] = distance[u]+1
    return distance[v2] is not None
    

def collectTranslations(numTrans):
    translations = []
    for i in range(0, ord('z')-ord('a')+1):
        translations.append([])
    for _ in range(numTrans):
        translation = [ord(x)-ord('a') for x in input().split()]
        translations[translation[0]].append(translation[1])
    return translations

def isMatch(w1, w2, translations):
    if len(w1) != len(w2):
        return False
    for i in range(len(w1)):
        if w1[i] != w2[i] and not (isPath(w1[i], w2[i], translations) or isPath(w1[i], w2[i], translations)):
            return False
    return True

def main():

    params = input().split()
    m = int(params[0])
    n = int(params[1])
    translations = collectTranslations(m)
    for _ in range(n):
        words = input().split()
        w1 = [ord(x)-ord('a') for x in words[0]]
        w2 = [ord(x)-ord('a') for x in words[1]]
        if isMatch(w1, w2, translations):
            print("yes")
        else:
            print("no")
main()
