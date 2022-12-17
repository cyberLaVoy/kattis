
def display(layout):
    for i in range(len(layout)):
        string = ""
        for j in range(len(layout[0])):
            string += layout[i][j]
        print(string)

words = input().split()

horizontal = words[0]
vertical = words[1]

layout = []
for i in range(len(vertical)):
    layout.append(['.']*len(horizontal))

vIndex = -1
hIndex = -1
found = False
for i in range(len(horizontal)):
    if found:
        break
    for j in range(len(vertical)):
        if vertical[j] == horizontal[i]:
            vIndex = j
            hIndex = i
            found = True
            break

for i in range(len(vertical)):
    layout[i][hIndex] = vertical[i]
for j in range(len(horizontal)):
    layout[vIndex][j] = horizontal[j]
display(layout)