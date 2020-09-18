#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>

int main() {
    int n, k, prevti, currti;
    std::queue<int> processing;
    std::cin >> n >> k;
    int maxoverlap = -1;
    int overlap;
    for (int i = 1; i <= n; i++) {
        std::cin >> currti;
        if (i == 1) 
            processing.push(currti);
        else if (currti-prevti < 1000)
            processing.push(currti);
        if(currti - processing.front() >= 1000)
            processing.pop();
        overlap = processing.size();
        if (overlap > maxoverlap)
            maxoverlap = overlap;
        prevti = currti;
    }
    std::cout << ceil( (double)maxoverlap/(double)k ) << std::endl;
    return 0;
}