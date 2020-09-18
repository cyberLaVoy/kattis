#include <iostream>
#include <string>
#include <math.h>

int main() {
    int depth;
    std::string directions;
    std::cin >> depth;
    std::cin >> directions;
    int index = 1; // start at root
    for (int i = 0; i < (int)directions.length(); i++) {
        if (directions[i] == 'R') {
            index = index*2+1;
        }
        else {
            index = index*2;
        }
    }
    int rootNumber = pow(2, depth+1)-1;
    int nodeNumber = rootNumber - index + 1;
    std::cout << nodeNumber << std::endl;
    return 0;
}