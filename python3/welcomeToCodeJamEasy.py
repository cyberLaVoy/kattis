
def solve():
    phrase = "welcome to code jam"
    numTests = int(input())

    for i in range(numTests):
        letters = input()
        letters = [l for l in letters]
        phraseCount = findPhraseCount(...) # what to do?
        print(phraseCount)
solve()

