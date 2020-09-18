#include <iostream>
#include <bitset>
#include <vector>

// bitset version
/*
const int maxPrime = 100000001;
std::bitset<maxPrime> isPrime;
void sieveOfEratosthenes() {
    isPrime.flip();
    isPrime[0] = false;
    isPrime[1] = false;
    for (int p = 2; p*p < maxPrime; p++) {
        if (isPrime[p]) {
            for (int i = p*p; i < maxPrime; i+=p) {
                isPrime[i] = false;
            }
        }
    }
}
*/

// vector version
std::vector<bool> sieveOfEratosthenes(int n, int& primeCount) {
    std::vector<bool> isPrime(n+1);
    isPrime.flip();
    isPrime[0] = false;
    isPrime[1] = false;
    primeCount -= 1;
    for (int p = 2; p*p <= n; p++) {
        if (isPrime[p]) {
            for (int i = p*p; i <= n; i+=p) {
                if (isPrime[i]) {
                    isPrime[i] = false;
                    primeCount--;
                }
            }
        }
    }
    return isPrime;
}
int main() {
    //sieveOfEratosthenes();
    int n, q, x;
    std::cin >> n >> q;
    int primeCount = n;
    std::vector<bool> isPrime = sieveOfEratosthenes(n, primeCount);
    std::cout << primeCount << std::endl;
    for (int i = 0; i < q; i++) {
        std::cin >> x;
        std::cout << isPrime[x] << std::endl;
    }
    return 0;
}
