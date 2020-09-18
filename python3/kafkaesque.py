

n = int(input())


passes = 1

cur = int(input())
nxt = None
for i in range(1, n):
    nxt = int(input()) 
    if nxt < cur:
        passes += 1
    cur = nxt

print(passes)
