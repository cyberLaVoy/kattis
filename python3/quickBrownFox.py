
numPhrases = int(input())

for i in range(numPhrases):
    missing = []
    found = [False]*26
    phrase = input()
    for l in phrase:
        value = ord(l.lower())-97
        if value >= 0 and value <= 25:
            found[value] = True
    for i in range(len(found)):
        if not found[i]:
            missing.append(i)
    if len(missing) == 0:
        print("pangram")
    else:
        string = "missing "
        for v in missing:
            string += chr(v+97)
        print(string)