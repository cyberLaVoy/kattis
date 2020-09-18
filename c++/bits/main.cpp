#include <iostream>
#include <bitset>
#include <string>

int maxNumBits(int value) {
    std::string strValue = std::to_string(value);
    std::bitset<32> bits;
    int max = 0;
    for (int i = 1; i <= (int) strValue.length(); i++) {
        std::string subString = strValue.substr(0,i);
        std::bitset<32> bits(std::stoi(subString));
        int total = bits.count();
        if (total > max) {
            max = total;
        }
    }
    return max;
}
int main() {
    int numTests;
    std::cin >> numTests;
    int value;
    for (int test = 0; test < numTests; test++) {
        std::cin >> value;
        std::cout << maxNumBits(value) << std::endl;
    }
    return 0;
}