#include <iostream>
#include <math.h>

int main() {
    int K;
    std::cin >> K;
    int barSize = pow(2, ceil(log2(K)));
    int breaks = 0;
    if ( (K & 1) == 1) {
        breaks = ceil(log2(K));
    }
    else if (K == barSize) {
        breaks = 0;
    }
    else {
        int total = 0;
        int temp = barSize;
        while (total != K) {
            temp = temp >> 1;
            breaks += 1;
            if (total + temp <= K) {
                total += temp;
            }
        }
    }


    std::cout << barSize << ' ' << breaks << '\n';
    return 0;
}