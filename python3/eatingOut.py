

params = input().split()
params = [int(x) for x in params]

if sum(params[1:]) <= 2*params[0]:
    print("possible")
else:
    print("impossible")
