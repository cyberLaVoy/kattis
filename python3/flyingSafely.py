import sys
data = sys.stdin.readlines()
numTests = int(data[0].strip())

paramsIndex = 1
for i in range(numTests):
    params = data[paramsIndex].strip().split()
    numVertices = int(params[0])
    numEdges = int(params[1])
    print(numVertices-1)
    paramsIndex += numEdges+1
