
characters = input()

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0

for char in characters:
    if char == '_':
        whitespace += 1
    elif ord(char) >= 97 and ord(char) <= 122: 
        lowercase += 1
    elif ord(char) >= 65 and ord(char) <= 90:
        uppercase += 1
    else:
        symbols += 1

print(whitespace/len(characters))
print(lowercase/len(characters))
print(uppercase/len(characters))
print(symbols/len(characters))

