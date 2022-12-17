
def longestLoop(segments):
    blue = []
    red = []
    for segment in segments:
        length = int(segment[:-1])
        if segment[-1] == 'R':
            red.append(length)
        else:
            blue.append(length)
    blue.sort()
    red.sort()
    loop = []
    while not (len(blue) == 0 or len(red) == 0):
        loop.append(blue.pop())
        loop.append(red.pop())
    loopLength = 0
    for segment in loop:
        loopLength += segment
        loopLength -= 1
    return loopLength


def solve():
    numTests = int(input())

    for i in range(numTests):
        input() # discard number of segments
        segments = input().split()
        print("Case #" + str(i+1) + ':', longestLoop(segments))

solve()
