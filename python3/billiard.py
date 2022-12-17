import math

def main():
    while True:
        a, b, s, m, n = map(int, input().split())
        if a == b == s == m == n == 0:
            break
        print("{:.2f} {:.2f}".format(180/math.pi*math.atan2(b*n, a*m), math.sqrt((n*b)**2 + (m*a)**2)/s))
main()
