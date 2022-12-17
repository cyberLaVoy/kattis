#include <iostream>
#include <string>
bool isOne(char c) {
    return c == '1';
}
bool isZero(char c) {
    return c == '0';
}
bool eitherIsQMark(char c0, char c1) {
    return c0 == '?' || c1 == '?';
}
void performInstruction(std::string& bits) {
    int i, j;
    std::string instruction;
    std::cin >> instruction;
    if (instruction == "CLEAR") {
        std::cin >> i;
        i = 31 - i;
        bits[i] = '0';
    }
    else if (instruction == "SET") {
        std::cin >> i;
        i = 31 - i;
        bits[i] = '1';
    }
    else if (instruction == "OR") {
        std::cin >> i >> j;
        i = 31 - i;
        j = 31 - j;
        if (!eitherIsQMark(bits[i], bits[j])) {
            bool result = isOne(bits[i]) || isOne(bits[j]);
            if (result) {
                bits[i] = '1';
            }
            else {
                bits[i] = '0';
            }
        }
        else {
            if (isOne(bits[i]) || isOne(bits[j])) {
                bits[i] = '1';
            }
            else {
                bits[i] = '?';
            }
        }
    }
    else if (instruction == "AND") {
        std::cin >> i >> j;
        i = 31 - i;
        j = 31 - j;
        if (!eitherIsQMark(bits[i], bits[j])) {
            bool result = isOne(bits[i]) && isOne(bits[j]);
            if (result) {
                bits[i] = '1';
            }
            else {
                bits[i] = '0';
            }
        }
        else {
            if (isZero(bits[i]) || isZero(bits[j])) {
                bits[i] = '0';
            }
            else {
                bits[i] = '?';
            }
        }
    }
}
int main() {
    int numInstructions;
    std::cin >> numInstructions;
    while (numInstructions != 0) {
        std::string bits = "????????????????????????????????";
        for (int i = 0; i < numInstructions; i++) {
            performInstruction(bits);
        }
        std::cout << bits << std::endl;
        std::cin >> numInstructions;
    }
    return 0;
}