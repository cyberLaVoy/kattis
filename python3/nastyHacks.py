
numCase = int(input())

for i in range(numCase):
    case = input().split(' ')
    r = int(case[0])
    e = int(case[1])
    c = int(case[2])
    if r < e - c:
        print("advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("do not advertise")