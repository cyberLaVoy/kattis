
pieces = input().split()

X = int(pieces[0])
Y = int(pieces[1])

numSplits = X*4 + Y*3

if numSplits & 1 == 1:
    print("impossible")
else:
    print("possible")