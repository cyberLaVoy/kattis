
quadkey = input()

x = 0
y = 0
for i in range(len(quadkey)):
    l = quadkey[i]
    n = len(quadkey) - i
    if l == '1' or l == '3':
        x += 2**n//2
    if l == '2' or l == '3':
        y += 2**n//2
print(len(quadkey), x, y)
