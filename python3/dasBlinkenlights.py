
def main():
    params = input().split()
    p = int(params[0])
    q = int(params[1])
    s = int(params[2])
    state = [False, False]
    for i in range(1, s+1):
        if i % p == 0:
            state[0] = not state[0]
        if i % q == 0:
            state[1] = not state[1]
        if state[0] and state[1]:
            print("yes")
            return
        state = [False, False]
    print("no")


main()