
chicken = input().split()

N = int(chicken[0])
M = int(chicken[1])

P = M - N

if P == 1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
elif P == -1:
    print("Dr. Chaz needs 1 more piece of chicken!")
elif P > 1 or P == 0:
    print("Dr. Chaz will have", P, "pieces of chicken left over!")
elif P < 0:
    print("Dr. Chaz needs", abs(P), "more pieces of chicken!")
