

def whatDoesTheFoxSay(cleanRecording):
    vocal = ""
    for sound in cleanRecording:
        if sound != '':
            vocal += (sound + ' ')
    print(vocal)
def solve():
    numTests = int(input())
    for i in range(numTests):
        recording = input().split(' ')
        knownSounds = []
        while True:
            soundInfo = input()
            if soundInfo == "what does the fox say?":
                break
            soundInfo = soundInfo.split(' ')
            knownSounds.append(soundInfo[2])
        for sound in knownSounds:
            for j in range(len(recording)):
                if sound == recording[j]:
                    recording[j] = ''
        whatDoesTheFoxSay(recording)
solve()