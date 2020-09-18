#include <iostream>
#include <string>

int main() {
    int capacity, stations, exited, entered, stayed;
    std::cin >> capacity >> stations;
    int onBoard = 0;
    std::string status = "possible";
    for (int i = 0; i < stations; i++) {
        std::cin >> exited >> entered >> stayed;
        if (exited > onBoard) {
           status = "impossible"; 
           break;
        }
        onBoard -= exited; 
        onBoard += entered;
        if (onBoard > capacity) {
           status = "impossible"; 
           break;
        }
        if (onBoard < capacity && stayed > 0) {
           status = "impossible"; 
           break;
        }
    }
    if (onBoard != 0) {
        status = "impossible";
    }
    std::cout << status << std::endl;
    return 0;
}