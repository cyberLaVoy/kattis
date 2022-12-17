

def longestIncreasingSubsequence(sequence):
    subSequenceLengths = [1]*len(sequence)
    for i in range(len(sequence)):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                subSequenceLengths[i] = max(subSequenceLengths[i], 1+subSequenceLengths[j])
    maximum = max(subSequenceLengths)
    subSequence = []
    for i in range(len(subSequenceLengths)-1, -1, -1):
        if subSequenceLengths[i] == maximum:
            subSequence.append(sequence[i])
            maximum = subSequenceLengths[i]-1
    subSequence.reverse()
    return subSequence

def main():
        word = input()

        # problem reduction
        sequence = []
        for l in word:
            sequence.append(ord(l))

        print(26-len(longestIncreasingSubsequence(sequence)))
main()