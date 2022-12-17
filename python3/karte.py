

def cardCount(cards):
    total = 0
    for b in cards:
        if b:
            total += 1
    return total
def cardsFound(cards, P, K, H, T):
    for i in range(0,len(cards),3):
        letter = cards[i]
        number = int(cards[i+1:i+3])
        if letter == 'P':
            if P[number-1] == True:
                print("GRESKA")
                return False
            P[number-1] = True
        if letter == 'K':
            if K[number-1] == True:
                print("GRESKA")
                return False
            K[number-1] = True
        if letter == 'H':
            if H[number-1] == True:
                print("GRESKA")
                return False
            H[number-1] = True
        if letter == 'T':
            if T[number-1] == True:
                print("GRESKA")
                return False
            T[number-1] = True
    return True

def solve():
    P = [False]*13
    K = [False]*13
    H = [False]*13
    T = [False]*13

    cards = input()
    if not cardsFound(cards, P, K, H ,T):
        return False

    Ptotal = cardCount(P)
    Ktotal = cardCount(K)
    Htotal = cardCount(H)
    Ttotal = cardCount(T)
    print(13-Ptotal, 13-Ktotal, 13-Htotal, 13-Ttotal)
solve()
