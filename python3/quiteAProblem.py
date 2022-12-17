import sys

count = 0
line = sys.stdin.readline()
while line != '':
    line = line.lower()
    if "problem" in line:
        print("yes")
    else:
        print("no")
    line = sys.stdin.readline()