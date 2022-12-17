from fractions import Fraction

input() # discard number of rings input

rings = input().split()
first = int(rings[0])

for i in range(1, len(rings)):
    ring = int(rings[i])
    turns = Fraction(first/ring).limit_denominator()
    string = str(turns)
    if '/' not in string:
        string += "/1"
    print(string)