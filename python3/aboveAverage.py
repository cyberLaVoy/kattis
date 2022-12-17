import math

numTests = int(input())

for i in range(numTests):
    scores = input().split()
    scores = scores[1:]
    scores = [int(x) for x in scores]
    averageScore = sum(scores)/len(scores)
    aboveAverageCount = 0
    for score in scores:
        if score > averageScore:
            aboveAverageCount += 1
    aboveAveragePercentage = round(100*(aboveAverageCount/len(scores)), 3)
    parts = str(aboveAveragePercentage).split('.')
    while len(parts[1]) < 3:
        parts[1] += '0'
    aboveAveragePercentage = parts[0] + '.' + parts[1] + '%'
    print(aboveAveragePercentage)
