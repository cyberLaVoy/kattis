

parameters = input().split()

R = int(parameters[0])
C = int(parameters[1])
Zr = int(parameters[2])
Zc = int(parameters[3])

article = []
for i in range(R):
    row = input()
    modifiedRow = ""
    for j in range(len(row)):
        modifiedRow += row[j]*Zc
    for j in range(Zr):
        article.append(modifiedRow)

for row in article:
    print(row)