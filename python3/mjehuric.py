
def displayList(obj):
    string = ""
    for item in obj:
        string += str(item) + ' '
    print(string[:len(string)-1])

def bubbleSort(obj):
    changeMade = True
    while changeMade:
        changeMade = False
        for i in range(len(obj)-1):
            if obj[i] > obj[i+1]:
                obj[i], obj[i+1] = obj[i+1], obj[i]
                changeMade = True
                displayList(obj)

def solve():
    obj = input().split()
    obj = [int(x) for x in obj]
    bubbleSort(obj)
solve()


