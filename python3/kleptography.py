
params = input().split()
prefixLength = int(params[0])

lastLetters = input()
ciphertext = input()
ciphertext = [ord(l)-ord('a') for l in ciphertext]
ciphertext.reverse()

plainText = [ord(l)-ord('a') for l in lastLetters]
plainText.reverse()
 
for i in range(len(ciphertext)):
    a = (ciphertext[i] - plainText[i]) % 26
    plainText.append(a)

key = ""
while len(plainText) != 0:
    key += chr(plainText.pop()+ord('a'))
message = key[prefixLength:]
print(message)

    



#   shortkeyword
# + zshortkeywor  
#   ------------
#   fzvfkdocukfu