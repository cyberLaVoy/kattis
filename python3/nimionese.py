
hardConsonats = "bcdgknpt"

def closestFirstLetter(letter):
    letter = letter.lower()
    closestLetter = 'b' 
    closestDistanct = abs(ord(letter) - ord('b'))
    for consonant in hardConsonats:
        distance = abs(ord(letter) - ord(consonant))
        if distance < closestDistanct:
            closestDistanct = distance
            closestLetter = consonant
    return closestLetter

def closestLastLetter(letter):
    letter = letter.lower()
    suffixes = ["ah", "oh", "uh"]
    closestSuffix = 'ah' 
    closestDistanct = abs(ord(letter) - ord('a'))
    for suffix in suffixes:
        distance = abs(ord(letter) - ord(suffix[0]))
        if distance < closestDistanct:
            closestDistanct = distance
            closestSuffix = suffix
    return closestSuffix

def translate(phrase):
    translated = ""
    for word in phrase:
        parts = word.split('-')
        firstLetter = parts[0][0]
        translatedWord = ""
        if firstLetter not in hardConsonats:
            letter = closestFirstLetter(firstLetter)
        else:
            letter = firstLetter
        for i in range(len(parts)):
            if i == 0:
                translatedPart = letter + parts[i][1:]
            else:
                translatedSubPart = ""
                for j in range(len(parts[i])):
                    if parts[i][j] in hardConsonats:
                        translatedSubPart += letter
                    else:
                        translatedSubPart += parts[i][j]
                translatedPart = translatedSubPart
            translatedWord += translatedPart
        lastLetter = translatedWord[-1]
        if lastLetter in hardConsonats:
            translatedWord += closestLastLetter(lastLetter)
        translated += translatedWord + ' '
    translated = translated[0].upper() + translated[1:]
    return translated
            

def solve():
    phrase = input().split()
    print(translate(phrase))
solve()