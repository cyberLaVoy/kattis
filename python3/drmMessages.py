

def rotate(half):
    half = [ord(c)-65 for c in half]
    rotation = sum(half)
    half = [(v+rotation)%26 for v in half]
    return half

def decrypt(firstHalf, secondHalf):
    for i in range(len(firstHalf)):
        firstHalf[i] = (firstHalf[i]+secondHalf[i])%26
    decrypted = ""
    for v in firstHalf:
        decrypted += chr(v+65)
    return decrypted

def solve():
    encrypted = input()

    firstHalf = encrypted[:len(encrypted)//2]
    firstHalf = rotate(firstHalf)
    secondHalf = encrypted[len(encrypted)//2:]
    secondHalf = rotate(secondHalf)
    decrypted = decrypt(firstHalf, secondHalf)
    print(decrypted)
solve()
