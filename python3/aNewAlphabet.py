
translation = {'a':"@", 'b':'8', 'c':'(', 'd': '|)', 'e':'3', 'f':'#', 'g':'6', 'h':'[-]', 'i':'|', 'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\/[]', 'n':'[]\[]', 'o':'0', 'p':'|D', 'q':'(,)', 'r':'|Z', 's':'$', 't':"']['", 'u':'|_|', 'v':'\/', 'w':'\/\/', 'x':'}{', 'y':'`/', 'z':'2'}

phrase = input().lower()

string = ""
for l in phrase:
    if l in translation:
        string += translation[l]
    else: 
        string += l
print(string)