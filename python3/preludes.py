import sys

alts = {"A#":"Bb", "C#":"Db", "D#":"Eb", "F#":"Gb", "G#":"Ab", "Bb":"A#", "Db":"C#", "Eb":"D#", "Gb":"F#", "Ab":"G#"}

caseNum = 1
for key in sys.stdin:
    key = key.strip().split(' ')
    if key[0] in alts:
        print("Case "+str(caseNum)+':', alts[key[0]], key[1])
    else:
        print("Case "+str(caseNum)+':',"UNIQUE")
    caseNum += 1