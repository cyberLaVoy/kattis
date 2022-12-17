
def mirrorImage(image):
    for i in range(len(image)-1,-1,-1):
        row = ""
        for j in range(len(image[0])-1,-1,-1):
            row += image[i][j]
        print(row)

def solve():
    numTests = int(input())
    for i in range(1, numTests+1):
        print("Test", i)
        params = input().split()
        numRows = int(params[0])
        image = []
        for j in range(numRows):
            row = input()
            row = [o for o in row]
            image.append(row)
        mirrorImage(image)
solve()