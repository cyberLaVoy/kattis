
def countFlys(section):
    count = 0
    for i in range(1, len(section)-1):
        for j in range(1, len(section[i])-1):
            if section[i][j] == '*':
                count += 1
    return count

def formatWindow(window, top, left, square):
    bottom = top+square-1
    right = left+square-1
    window[top] = window[top][:left] + ['+'] + ['-']*(square-2) + ['+']  + window[top][left+square:]
    window[bottom] = window[bottom][:left] + ['+'] + ['-']*(square-2) + ['+']  + window[bottom][left+square:]
    for i in range(top+1, bottom):
        window[i] = window[i][:left] + ['|'] + window[i][left+1:right]  + ['|'] + window[i][right+1:]
    for i in range(len(window)):
        string = ""
        for j in range(len(window[i])):
            string += window[i][j]
        print(string)

def solve():
    params = input().split()

    rows = int(params[0])
    cols = int(params[1])
    square = int(params[2])

    window = []
    for i in range(rows):
        row = input()
        row = [l for l in row]
        window.append(row)

    maxCount = 0
    maxI = -1
    maxJ = -1
    for i in range(rows-square+1):
        for j in range(cols-square+1):
            section = window[i:square+i]
            section = [row[j:square+j] for row in section]
            count = countFlys(section)
            if count > maxCount:
                maxCount = count
                maxI = i
                maxJ = j
    print(maxCount)
    formatWindow(window, maxI, maxJ, square)

solve()