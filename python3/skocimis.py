
kangaroos = input().split()

a = int(kangaroos[0])
b = int(kangaroos[1])
c = int(kangaroos[2])

best = max(b-a, c-b)
print(best-1)
