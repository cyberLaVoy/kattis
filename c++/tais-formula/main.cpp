#include <iostream>
#include <iomanip>

int main() {
    int N;
    std::cin >> N;
    double curti, curvi;
    double prevti = -1;
    double prevvi = -1;
    double area = 0;
    for (int i = 0; i < N; i++) {
        std::cin >> curti >> curvi;
        if (! (prevti == -1 && prevvi == -1) ) {
            area += ( (curvi+prevvi)/2 * (curti-prevti) );
        }
        prevti = curti;
        prevvi = curvi;

    }
    area /= 1000;
    std::cout << std::setprecision(7) << area << std::endl;
    return 0;
}