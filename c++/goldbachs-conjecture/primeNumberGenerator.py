import math

def isPrime(n):
    if (n == 1):
        return False
    if (n == 2 or n == 3):
        return True
    if (n & 1 != 1):
        return False
    upper = math.ceil(math.sqrt(n))+1
    for i in range(3, upper, 2):
        if (n % i == 0):
            return False
    return True

def genPrimes():
    primes = [2]
    for n in range(3, 100000001, 2):
        if (isPrime(n)):
            primes.append(n)
    print(primes)
    print(len(primes))
genPrimes()


