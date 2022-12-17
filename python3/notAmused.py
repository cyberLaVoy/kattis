import sys

def solve():
    day = 1
    while True:
        entry = sys.stdin.readline().strip() # OPEN
        if entry == '':
            break
        if day != 1:
            print()

        logs = {}
        entry = sys.stdin.readline().strip()
        while entry != 'CLOSE':
            entry = entry.split()
            action = entry[0]
            name = entry[1]
            time = int(entry[2])
            if name in logs: 
                if action == "ENTER":
                    logs[name]["ENTER"] = time
                else:
                    logs[name]["TIME"] += time - logs[name]["ENTER"]
            else:
                logs[name] = {"TIME":0, "ENTER":time}
            entry = sys.stdin.readline().strip()

        print("Day", day)
        sortedNames = [key for key in logs]
        sortedNames.sort()
        for name in sortedNames:
            charge = str(round(.1*logs[name]["TIME"],2)).split('.')
            while len(charge[1]) < 2:
                charge[1] += '0'
            charge = charge[0] + '.' + charge[1]
            print(name, '$'+charge)
        day += 1
        
solve()
