
numStars = int(input())
print(numStars,':',sep='')
for i in range(1, numStars//2+1):
    if numStars % i == 0 and i != 1:
        print(i,',',i,sep='')
    if (numStars-(i+1)) % (2*i+1) == 0:
        print(i+1,',',i,sep='')
    if numStars % (2*i+1) == 0:
        print(i+1,',',i,sep='')
        
    