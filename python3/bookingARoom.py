
def findRoom(bookedList):
    for i in range(len(bookedList)):
        if not bookedList[i]:
            print(i+1)
            return
    print("too late")

def solve():
    params = input().split()

    available = int(params[0])
    taken = int(params[1])

    bookedList = [False]*available
    for i in range(taken):
        bookedList[int(input())-1] = True
    findRoom(bookedList)
solve()