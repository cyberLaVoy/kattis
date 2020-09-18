
params = input().split(' ')

l = int(params[0])
hor = int(params[1])
ver = int(params[2])

mHor = max( hor, abs(l-hor))
mVer = max( ver, abs(l-ver))

print(4*mHor*mVer)