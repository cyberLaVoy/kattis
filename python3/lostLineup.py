
n = int(input())

order = [None]*n
order[0] = 1

people = [int(x) for x in input().split()]

for i in range(len(people)):
    index = people[i]+1
    order[index] = i+2

print(" ".join([str(v) for v in order]))