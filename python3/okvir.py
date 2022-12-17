
wordParams = input().split()
M = int(wordParams[0])
N = int(wordParams[1])
paddingParams = input().split()

U = int(paddingParams[0])
L = int(paddingParams[1])
R = int(paddingParams[2])
D = int(paddingParams[3])

rows = U+M+D
cols = L+N+R

words = []
for i in range(M):
    words.append(input())

board = []
for i in range(rows):
    row = []
    if i & 1 == 1:
        a = '.'
        b = '#'
    else:
        b = '.'
        a = '#'
    for j in range(cols):
        if j & 1 == 1:
            row.append(b)
        else:
            row.append(a)
    board.append(row)

wordIndex = 0
for i in range(U, U+M):
    word = words[wordIndex]
    for j in range(L,L+N):
        board[i][j] = word[j-L]
    wordIndex += 1

for row in board:
    for l in row:
        print(l, end='')
    print()
