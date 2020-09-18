

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def SSD(b, n):
    translation = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    ssd = 0
    valueInBaseb = toStr(n, b)
    for l in valueInBaseb:
        if l in translation:
            l = translation[l]
        ssd += int(l)**2
    return ssd

def solve():
    numDataSets = int(input())
    for i in range(numDataSets):
        dataSet = input().split(' ')
        K = dataSet[0]
        b = int(dataSet[1])
        valueInBase10 = int(dataSet[2])
        print(K, SSD(b, valueInBase10))
solve()

