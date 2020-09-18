import sys

inputValues = sys.stdin.readline().strip().split(' ')
articlesPublished = int(inputValues[0])
impactFactor = int(inputValues[1])

minImpactFactor = impactFactor - 1
minCitations = articlesPublished*minImpactFactor+1

print(minCitations)
