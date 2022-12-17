
def crossOffLetter(word, letter):
    totalCrosses = 0
    for i in range(len(word)):
        if letter == word[i]:
            totalCrosses += 1
    return totalCrosses

def main():
    word = input()
    sequence = input()

    totalCrossedOff = 0
    totalWrongGuesses = 0
    for l in sequence:
        numCrossedOff = crossOffLetter(word, l)
        totalCrossedOff += numCrossedOff
        if numCrossedOff == 0:
            totalWrongGuesses += 1

        if totalCrossedOff == len(word):
            print("WIN")
            break
        if totalWrongGuesses == 10:
            print("LOSE")
            break
main()