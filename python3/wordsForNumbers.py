import sys

def convert(number):
    translation = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven",12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
    number = str(number)
    number = [int(x) for x in number]
    if len(number) == 1:
        return translation[number[0]]
    else:
        tensPlace = number[0]
        onesPlace = number[1]
        if tensPlace == 1:
            return translation[tensPlace*10+onesPlace]
        else:
            string = translation[tensPlace*10]
            if onesPlace != 0:
                string += '-' + translation[onesPlace]
            return string


def solve():
    for line in sys.stdin:
        line = line.split()
        newLine = ""
        for word in line:
            if word.isdigit():
                word = convert(word)
            newLine += word + ' '
        newLine = newLine[0].upper() + newLine[1:]
        sys.stdout.write(newLine+'\n')
solve()