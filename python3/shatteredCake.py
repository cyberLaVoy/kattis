import sys


width = int(input())
input() # discard number of pieces

pieces = sys.stdin.readlines()

totalArea = 0
for pieceDimen in pieces:
    pieceDimen = pieceDimen.split() 
    w = int(pieceDimen[0])
    l = int(pieceDimen[1])
    totalArea += w*l

print(totalArea//width)