import sys

levels = sys.stdin.readline().strip()
while levels != '':
    levels = int(levels)
    line = input()
    string = ""
    for l in line:
        v = ord(l)
        if v >= 33 and v <= 42 or v >= 91 and v <= 93:
            if levels > 0:
                string += "\\"
            if levels > 1:
                string += "\\\\"*(2**(levels-1)-1)

        string += l
    print(string)
    levels = sys.stdin.readline().strip()