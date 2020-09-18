

def appendNames(Y, P):
    l = Y[-1]
    if l == 'e':
        appended = Y+"x"+P
    elif l in "aiou":
        appended = Y[:-1]+"ex"+P
    elif Y[-2:] == "ex":
        appended = Y+P
    else:
        appended = Y+"ex"+P
    return appended


def main():
    Y, P = input().split()
    appended = appendNames(Y, P)
    print(appended)
main()

