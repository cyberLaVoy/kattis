import math

params = input().split()
red = int( params[0] )
brown = int( params[1] )

a = int(math.sqrt(brown))
b = brown/a

dimens = [int(a+2), int(b+2)]
dimens.sort(reverse=True)
print(dimens[0], dimens[1])
