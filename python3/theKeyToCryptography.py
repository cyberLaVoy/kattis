
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translation = {l:ord(l)-65 for l in letters}
ciphertext = input()
secret = input()
message = ""

i = 0
while i < len(secret) and i < len(ciphertext):
    cipherAscii = translation[ciphertext[i]]
    rotation = 26-translation[secret[i]]
    rotated = (cipherAscii+rotation)%26
    char = chr(rotated + 65)
    message += char
    secret += char # this is the magic step
    i += 1
print(message)
