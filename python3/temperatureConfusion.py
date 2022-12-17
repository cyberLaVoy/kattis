
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solve():
    frac = input().split('/')
    num = int(frac[0])
    den = int(frac[1])
    num -= 32*den
    num *= 5
    den *= 9
    common = gcd(num, den)
    C = str(int(num/common)) + '/' + str(int(den/common))
    print(C)
solve()