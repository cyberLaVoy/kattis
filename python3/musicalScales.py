
# used to generate keys dictinary
"""
keyboard = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
# tone, tone, semitone, tone, tone, tone, semitone
keySteps = [2, 4, 5, 7, 9, 11]
keys = {}
for i in range(len(keyboard)):
    key = [keyboard[i]]
    for step in keySteps:
        index = (i + step) % 12
        key.append(keyboard[index])
    keys[keyboard[i]] = key
print("keys =", keys)
"""

keys = {'G#': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'], 'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'], 'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'], 'C#': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'], 'A#': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'], 'F': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'], 'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'], 'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'], 'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'], 'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'], 'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']}
        
input() # discard number of notes

notes = input().split()

possibleKeys = []
for key in keys:
    inKey = True
    for note in notes:
        if note not in keys[key]: 
            inKey = False
            break
    if inKey:
        possibleKeys.append(key)

if len(possibleKeys) == 0:
    print("none")
else:
    possibleKeys.sort()
    possible = ""
    for key in possibleKeys:
        possible += key + ' '
    print(possible)

