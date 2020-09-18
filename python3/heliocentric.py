import sys

def daysUntil(earth, mars):
    days = 0
    while not (earth == 0 and mars == 0):
        earth = (earth+1)%365
        mars = (mars+1)%687
        days += 1
    return days

def main():
    params = sys.stdin.readline()
    case = 1
    while params != '':
        params = [int(x) for x in params.split()]
        print("Case", str(case)+':', daysUntil(params[0], params[1]))
        case += 1
        params = sys.stdin.readline()
main()
