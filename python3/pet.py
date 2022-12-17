
bestScore = 0
contestant = -1
for i in range(5):
    scores = input().split(' ')
    score = 0
    for j in range(len(scores)):
        score += int(scores[j])
    if score > bestScore:
        bestScore = score
        contestant = i+1
print(contestant, bestScore)
