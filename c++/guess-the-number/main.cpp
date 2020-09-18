#include <iostream>
#include <string>

int main() {
    std::string result; 
    int low = 1;
    int high = 1000;
    int guess = 500;
    std::cout << guess << '\n';
    std::cin >> result;
    while (result != "correct") {
        if (result == "lower") {
            high = guess-1;
        }
        else if (result == "higher") {
            low = guess+1;
        }
        guess = (high + low)/2;
        std::cout << guess << '\n';
        std::cin >> result;
    }
    return 0;
}