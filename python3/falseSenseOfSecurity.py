import sys

# used to create the tranlations
"""
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","..--",".-.-","---.","----"] 
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_,.?"
string = "{"
for i in range(len(morse)):
    string += '"' + morse[i] + '"' + ':' + '"' + alphabet[i] + '"' + ','
print(string[:len(string)-1]+'}')
string = "{"
for i in range(len(morse)):
    string += '"' + alphabet[i] + '"' + ':' + '"' + morse[i] + '"' + ','
print(string[:len(string)-1]+'}')
"""

mToA = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z","..--":"_",".-.-":",","---.":".","----":"?"}
aToM = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","_":"..--",",":".-.-",".":"---.","?":"----"}

encypted = sys.stdin.readline().strip()
while encypted != '':
    morseLengths = []
    code = ""
    for l in encypted: 
        part = aToM[l]
        code += part
        morseLengths.append(len(part))

    decrypted = ""
    start = 0
    for i in range(len(morseLengths)-1,-1,-1):
        length = morseLengths[i]
        part = code[start:start+length]
        start += length 
        decrypted += mToA[part]
    print(decrypted)

    encypted = sys.stdin.readline().strip()