import math

def kamenetskysFormula(n): # returns the number of digits for the given factorotial
    if (n <= 1): 
        return 1
    else:
        return math.ceil(n*math.log10(n/math.e) + math.log10(2*math.pi*n)/2)

def bruteForce(num):
    num = int(num)
    n = 1
    i = 1
    while n < num:
        i += 1   
        n *= i
    return i

# max n: 205022 (found by trial and error with Kamentsky's formula)
def solve():
    factorial = input()

    if len(factorial) <= 3:
        print(bruteForce(factorial))
    else: # preform binary search to match the number of digits in input
        low = 1
        high = 205024
        guess = high//2
        numDigitis = kamenetskysFormula(guess)
        while numDigitis != len(factorial): 
            if numDigitis < len(factorial): # guess too low
                low = guess + 1
            elif numDigitis > len(factorial): # guess to high
                high = guess - 1
            guess = (high + low)//2
            numDigitis = kamenetskysFormula(guess)

        print(int(guess))
solve()
