#include <iostream>
#include <math.h>

int main() {
    int numBridges;
    int numKnights;
    int numKnightsNeeded;
    std::cin >> numBridges;
    std::cin >> numKnights;
    std::cin >> numKnightsNeeded;

    int numGroups = numKnights / numKnightsNeeded;
    int numDays = 0;
    while (numBridges > 1) {
        numDays += 1;
        numBridges -= numGroups;
    }

    std::cout << numDays << '\n';
    return 0;
}