
def numComplete(tasks, T):
    for i in range(len(tasks)):
        T -= int(tasks[i])
        if T < 0:
            print(i)
            return
    print(len(tasks))

def solve():
    params = input().split()
    T = int(params[1])
    tasks = input().split()
    numComplete(tasks, T)
solve()

