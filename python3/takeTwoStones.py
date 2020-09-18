import sys

numStones = int(sys.stdin.readline())
if numStones & 1:
    print("Alice")
else:
    print("Bob")
