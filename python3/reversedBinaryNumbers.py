# solution 1
"""
number = int(input())

numSigBits = 0
temp = number
while temp != 0:
    temp = temp >> 1
    numSigBits += 1
binary = ""
for i in range(numSigBits):
    temp = number
    temp = temp >> 1
    temp = temp << 1
    if temp < number:
        binary += '1'
    else:
        binary += '0'
    number = number >> 1
print(int(binary, base=2))
"""

# solution 2
n = bin(int(input()))
r = n[2:][::-1]
print(int(r, 2))