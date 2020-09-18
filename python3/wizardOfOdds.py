import math

N, K = input().split()

if math.log2(int(N)) <= int(K):
    print("Your wish is granted!")
else:
    print("You will become a flying monkey!")