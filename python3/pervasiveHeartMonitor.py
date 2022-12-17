import sys

patient = sys.stdin.readline()
while patient != '':
    patient = patient.strip().split()
    name = []
    count = 0
    total = 0
    for v in patient:
        if ord(v[0]) >= 65 and ord(v[0]) <= 90 or ord(v[0]) >= 97 and ord(v[0]) <= 122:
            name.append(v)
        else:
            total += float(v)
            count += 1
    average = total/count
    string = str(average)
    for part in name:
        string += ' ' + part
    print(string)
    patient = sys.stdin.readline()