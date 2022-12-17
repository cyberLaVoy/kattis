import sys

def translate(phrase):
    vowels = "aeiouy"
    phrase = phrase.split()
    translated = ""
    for l in phrase:
        if l[0] in vowels:
            translated += l + "yay"
        else:
            for i in range(len(l)):
                if l[i] in vowels:
                    translated += l[i:] + l[:i] + "ay"
                    break
        translated += " "
    print(translated)

def solve():
    phrase = sys.stdin.readline().strip()
    while phrase != '':
        translate(phrase)
        phrase = sys.stdin.readline().strip()
solve()
