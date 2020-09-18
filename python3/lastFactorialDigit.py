import sys

def lastFactorialDigit(factorial):
    lastDigit = 1
    for i in range(1,factorial+1):
        lastDigit = (lastDigit*i) % 10
    return lastDigit

def main():
    numTests = int(sys.stdin.readline())
    for i in range(numTests):
        factorial = int(sys.stdin.readline())
        lastDigit = lastFactorialDigit(factorial)
        print(lastDigit)
main()

