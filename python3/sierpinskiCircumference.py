import sys, math


# p(n) = 3^(n+1) / 2^n 
#      = 3* 3^n / 2^n
#      = 3*(3/2)^n 
# log(p(n)) = log(3*(3/2)^n)
#          = log(3) + n*log(3/2)

i = 1
n = sys.stdin.readline()
while n != '':
    n = int(n)
    # how many zeros?
    zeros = int( math.log(3, 10) + n * math.log(3/2, 10) )
    print("Case " + str(i) + ':', zeros + 1)
    i += 1
    n = sys.stdin.readline()
