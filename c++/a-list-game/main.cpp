#include <iostream>
#include <math.h>
#include <vector>

// prime factorization
int main() {
    int X;
    std::cin >> X;
    std::vector<int> primeFactors;
    while ( (X & 1) != 1 ) {
        primeFactors.push_back(2);
        X = X >> 1;
    }
    for (int i = 3; i <= sqrt(X); i += 2) {
        while (X % i == 0) {
            primeFactors.push_back(i);
            X /= i;
        }
    }
    if (X > 1) {
        primeFactors.push_back(X);
    }
    std::cout << primeFactors.size() << std::endl;
    return 0;
}