

def invertCase(word):
    new = []
    for l in word:
        if ord(l) >= ord('a') and ord(l) <= ord('z'):
            new.append(l.upper())
        elif ord(l) >= ord('A') and ord(l) <= ord('Z'):
            new.append(l.lower())
        else:
            new.append(l)
    return "".join(new)
        


def isAcceptable(actual, submitted):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    if actual == submitted:
        return True
    elif actual[-1] in digits and actual[:-1] == submitted:
        return True
    elif actual[0] in digits and actual[1:] == submitted:
        return True
    elif actual == invertCase(submitted):
        return True
    else:
        return False


def main():
    S = input()
    P = input()
    if isAcceptable(S, P):
        print("Yes")
    else:
        print("No")
main()