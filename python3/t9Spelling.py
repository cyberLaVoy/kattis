
translation = {'a': 2, 'b': 22, 'c': 222, 'd': 3, 'e':33, 'f':333, 'g':4, 'h':44, 'i':444, 'j':5, 'k':55, 'l':555, 'm':6, 'n':66, 'o':666, 'p':7, 'q':77, 'r':777, 's':7777, 't':8, 'u':88, 'v':888, 'w':9, 'x':99, 'y':999,'z':9999, ' ':0}
numPhrases = int(input())

case = 1
for j in range(numPhrases):
    phrase = input()

    string = ""
    for i in range(len(phrase)-1):
        trans = str(translation[phrase[i]])
        nextTrans = str(translation[phrase[i+1]])
        string += trans
        if trans[0] == nextTrans[0]:
            string += ' '
    string += str(translation[phrase[-1]])
    print("Case #" + str(case) + ":", string)
    case += 1
    