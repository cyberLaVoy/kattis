
letterCounts = {}

word = input()
for l in word:
    if l in letterCounts:
        letterCounts[l] += 1
    else:
        letterCounts[l] = 1

letterCountsO = []
for l in letterCounts:
    if letterCounts[l] & 1 == 1:
        letterCountsO.append(letterCounts[l])
if len(letterCountsO) != 0:
    letterCountsO.pop()

removeCount = len(letterCountsO)
print(removeCount)