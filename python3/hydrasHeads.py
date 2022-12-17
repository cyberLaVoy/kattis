
def growHead(hydra):
    hydra[0] += 1
    hydra[1] -= 2
    hydra[2] += 1
def growTail(hydra):
    hydra[1] += 1
    hydra[2] += 1
def cutOffheads(hydra):
    hydra[0] -= 2
    hydra[2] += 1

def movesToDefeat(heads, tails):
    hydra = [heads, tails, 0]
    while True:
        while hydra[0] > 1:
            cutOffheads(hydra)
        if hydra[0] == 1:
            if hydra[1] == 0:
                return -1
            else:
                if hydra[1] >= 2:
                    growHead(hydra)
                else:
                    growTail(hydra)
        elif hydra[0] == 0: 
            if hydra[1] == 0:
                return hydra[2]
            else:
                while hydra[1] % 4 != 0:
                    growTail(hydra)
                while hydra[1] != 0:
                    growHead(hydra)


def solve():
    hydra = input().split()
    heads = int(hydra[0])
    tails = int(hydra[1])
    while not (heads == 0 and tails == 0):
        print(movesToDefeat(heads, tails))

        hydra = input().split()
        heads = int(hydra[0])
        tails = int(hydra[1])
solve()