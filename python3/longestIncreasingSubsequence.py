import sys

# sequence: a sorted or unsorted list of doubles or integers
# Output: an increasing subsequence that is of longest possible length
def longestIncreasingSubsequence(sequence):
    subSequenceLengths = [1]*len(sequence)
    for i in range(len(sequence)):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                subSequenceLengths[i] = max(subSequenceLengths[i], 1+subSequenceLengths[j])
    maximum = max(subSequenceLengths)
    subSequenceIndices = []
    for i in range(len(subSequenceLengths)-1, -1, -1):
        if subSequenceLengths[i] == maximum:
            subSequenceIndices.append(i)
            maximum = subSequenceLengths[i]-1
    subSequenceIndices.reverse()
    return subSequenceIndices

# sequence: a sorted or unsorted list of doubles or integers
# Output: an increasing subsequence that is of longest possible length
def longest_increasing_subsequence(sequence):
    sequenceLength = len(sequence)
    P = [0]*sequenceLength
    M = [0]*(sequenceLength+1)
    L = 0
    for i in range(sequenceLength):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (sequence[M[mid]] < sequence[i]):
               lo = mid+1
           else:
               hi = mid-1
       newL = lo
       P[i] = M[newL-1]
       M[newL] = i
       if newL > L:
           L = newL
    subsequenceIndices = []
    k = M[L]
    for i in range(L-1, -1, -1):
        subsequenceIndices.append(k)
        k = P[k]
    subsequenceIndices.reverse()
    return subsequenceIndices


def main():
    length = sys.stdin.readline()
    while length != '':
        sequence = [int(x) for x in input().split()]
        #subSequenceIndices = longestIncreasingSubsequence(sequence)
        subSequenceIndices = longest_increasing_subsequence(sequence)
        print(len(subSequenceIndices))
        print(" ".join(str(x) for x in subSequenceIndices))
        length = sys.stdin.readline()


if __name__ == "__main__":
    main()