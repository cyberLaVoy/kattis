
input()
busNumbers = input().split()
busNumbers = [int(x) for x in busNumbers]
busNumbers.sort()

bins = []
b = []
b.append(busNumbers[0])
for i in range(1,len(busNumbers)):
    if busNumbers[i]-1 == b[-1]:
        b.append(busNumbers[i])
    else:
        bins.append(b)
        b = []
        b.append(busNumbers[i])
bins.append(b)

string = ""
for b in bins:
    s = ""
    if len(b) >= 3:
        s = str(b[0]) + '-' + str(b[-1]) + ' '
    else:
        for num in b:
            s += str(num) + ' '
    string += s 
print(string)

    
