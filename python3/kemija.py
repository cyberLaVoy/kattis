
sentence = input()

vowels = ['a', 'e', 'i', 'o', 'u']
decoded = ""

i = 0
while i < len(sentence):
    decoded += sentence[i]
    if sentence[i] in vowels: 
        i += 2
    i += 1
print(decoded)