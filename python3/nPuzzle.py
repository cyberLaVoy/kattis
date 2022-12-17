

goal = [['A', 'B', 'C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','.']]
positions = {"A":[0,0],"B":[0,1],"C":[0,2],"D":[0,3],"E":[1,0],"F":[1,1],"G":[1,2],"H":[1,3],"I":[2,0],"J":[2,1],"K":[2,2],"L":[2,3],"M":[3,0],"N":[3,1],"O":[3,2],".":[3,3]}

# used to make positions dictionary
"""
string = "{"
for x in range(4):
    part = ""
    for y in range(4):
        part += '"' + goal[x][y] + '"' + ":[" + str(x) + ',' + str(y) + '],'
    string += part
print(string[:-1] + '}')
"""

current = []
for i in range(4):
    row = []
    for l in input():
        row.append(l)
    current.append(row)

scatter = 0
for x in range(4):
    for y in range(4):
        curLetter = current[x][y]
        if curLetter != goal[x][y] and curLetter != '.':
            dist = abs(x-positions[curLetter][0]) + abs(y-positions[curLetter][1])
            scatter += dist
print(scatter)