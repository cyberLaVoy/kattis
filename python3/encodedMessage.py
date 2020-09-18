import math

numTests = int(input())

for i in range(numTests):
    encoded = input()

    squareSide = int(math.sqrt(len(encoded)))
    graph = []
    k = 0
    for i in range(squareSide):
        row = [] 
        for j in range(squareSide): 
            row.append(encoded[k])
            k += 1
        graph.append(row)

    message = ""
    for j in range(len(graph[0])-1,-1,-1):
        for i in range(len(graph)): 
            message += graph[i][j]
        
    print(message)
