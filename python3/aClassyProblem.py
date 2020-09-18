
def convertClassToInt(clss):
    s = ""
    for c in clss.split('-'):
        if c == "upper":
            s += '3'
        if c == "middle":
            s += '2'
        if c == "lower":
            s += '1'
    s = s[::-1]
    return int(s+('2'*(10-len(s))))

def classPos(obj):
    return obj[1]
def namePos(obj):
    return obj[0]
        

def main():
    numCases = int(input())
    for _ in range(numCases):
        numPeople = int(input())
        people = []
        for _ in range(numPeople):
            info = input().split()
            name = info[0][:-1]
            clss = convertClassToInt(info[1])
            people.append( [name, clss] )
        people.sort(key=namePos)
        people.sort(key=classPos, reverse=True)
        for name, clss in people:
            print(name)
        print("==============================")
main()