#include <iostream>

void printBoard(int* board, int maxIndex) {
    for (int i = 1; i <= maxIndex; i++) {
        if( i-1 != 0 && (i-1)%10 == 0 ) {
            std::cout << std::endl;
        }
        std::cout << board[i] << ' ';
    }
    std::cout << std::endl;
}
int findWinnableBoard(int* board, int boardSize, int numCounters) {
    int maxIndex = 1;
    while (numCounters--) {
        for (int i = 1; i < boardSize; i++) {
            if ( board[i] == 0) {
                board[i] = i;
                if (i > maxIndex) {
                    maxIndex = i;
                }
                break;
            }
            else {
                board[i]--;
            }
        }
    }
    return maxIndex;
}
int main() {
    int numTests, testNum, numCounters;
    std::cin >> numTests;
    for (int i = 0; i < numTests; i++) {
        std::cin >> testNum >> numCounters;
        int boardSize = 81;
        int board[boardSize] = {0};
        int maxIndex = findWinnableBoard(board, boardSize, numCounters);
        std::cout << testNum << ' ' << maxIndex << std::endl;
        printBoard(board, maxIndex);
    }
    return 0;
}