
frame = [["..#..",".#.#.","#.X.#",".#.#.","..#.."],["..*..", ".*.*.", "*.X.*", ".*.*." ,"..*.."]]
rIndex = 2
cIndex = 2

word = input()

framed = []
for i in range(len(word)):
    if (i+1) % 3 == 0:
        wendyFrame = frame[1][:]
        wendyFrame[rIndex] = wendyFrame[rIndex][:cIndex] + word[i] + wendyFrame[rIndex][cIndex+1:]
        framed.append(wendyFrame)
    else:
        panFrame = frame[0][:]
        if i != 0 and i % 3 == 0:
            panFrame[rIndex] = '*' + panFrame[rIndex][1:cIndex] + word[i] + panFrame[rIndex][cIndex+1:]
        else:
            panFrame[rIndex] = panFrame[rIndex][:cIndex] + word[i] + panFrame[rIndex][cIndex+1:]
        framed.append(panFrame)

for i in range(len(framed[0])):
    string = ""
    for j in range(len(framed)):
        if j != len(framed)-1:
            for k in range(len(framed[j][i])-1):
                string += framed[j][i][k]
        else:
            for k in range(len(framed[j][i])):
                string += framed[j][i][k]
    print(string)

