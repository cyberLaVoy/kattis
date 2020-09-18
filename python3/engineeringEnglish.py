import sys

words = {}

for line in sys.stdin:
    line = line.strip().split()
    newLine = ""
    for word in line:
        lword = word.lower()
        if lword in words:
            newLine += '. '
        else:
            words[lword] = 1
            newLine += word + ' '
    print(newLine)

