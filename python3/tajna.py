import math

def getLargestDivisor(value):
    largest = 1
    for i in range(2, int(math.sqrt(value))+1):
        if value % i == 0 and i > largest:
            largest = i
    return largest

def decrypt(word):
    numRows = getLargestDivisor(len(word))
    numCols = len(word)//numRows
    decrypted = ""
    for i in range(numRows):
        for j in range(numCols):
            decrypted += word[i+numRows*j]
    return decrypted

def main():
    word = input()
    decrypted = decrypt(word)
    print(decrypted)

main()