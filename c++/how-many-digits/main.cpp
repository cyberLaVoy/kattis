#include <iostream>
#include <math.h>

// N! = ( N*(N-1)*(N-2)*...(N-(N-2))*(N-(N-1)) ) 
// ceil( log10(N!) ) = number of digits

int countingDigits(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    else {
        double totalOfLogs = 0;
        for (int i = 1; i <= n; i++) {
            totalOfLogs += log10(i);
        }
        return ceil(totalOfLogs);
    }
}

int kamenetskysFormula(int n) {
    if (n <= 1) {
        return 1;
    }
    else {
        return ceil(n*log10(n/M_E) + log10(2*M_PI*n)/2);
    }
}

int main() {
    int digit;
    while (std::cin >> digit) {
        std::cout << kamenetskysFormula(digit) << std::endl;
    }
    return 0;
}