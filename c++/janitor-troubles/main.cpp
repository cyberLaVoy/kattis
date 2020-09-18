#include <iostream>
#include <math.h>
#include <iomanip>
#include <limits>

int main() {
    double a, b, c, d;
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
    std::cin >> d;

    double s = (a+b+c+d)/2;
    double maximum = sqrt((s-a)*(s-b)*(s-c)*(s-d));

    //std::cout << std::setprecision(std::numeric_limits<long double>::digits10 + 1) << maximum << std::endl; // for maximum precision
    std::cout << std::setprecision(15) << maximum << std::endl;
    return 0;
}