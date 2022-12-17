

def solve():
    phrase = input().split()
    words = []
    for word in phrase:
        if word not in words:
            words.append(word)
        else:
            print("no")
            return
    print("yes")
    return
solve()
