import sys

words = sys.stdin.readline()
allWords = []
while words != '':
    words = words.strip().split()
    for i in range(len(words)):
        allWords.append(words[i])
    words = sys.stdin.readline()

possible = []
for i in range(len(allWords)):
    for j in range(i+1,len(allWords)):
        combo = allWords[i] + allWords[j]
        possible.append(combo)
for i in range(len(allWords)-1,-1,-1):
    for j in range(i-1,-1,-1):
        combo = allWords[i] + allWords[j]
        possible.append(combo)

possible = list(set(possible))
possible.sort()
for word in possible:
    print(word)
