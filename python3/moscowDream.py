

params = [int(x) for x in input().split()]
n = params.pop()

if ( n < 3 ) or ( 0 in params ) or sum(params) < n:
    print("NO")
else:
    print("YES")

