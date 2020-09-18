#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int numPeopleInQueue;
    int minutesUntilClosed;
    std::cin >> numPeopleInQueue;
    std::cin >> minutesUntilClosed;
    int moneyAmount;
    int timeUntilLeave;
    int maxTimeUntilLeave = -1;
    std::vector<std::vector<int>> subQueues;
    for (int i = 0; i < numPeopleInQueue; i++) {
        std::cin >> moneyAmount;
        std::cin >> timeUntilLeave;
        while ((int)subQueues.size() <= timeUntilLeave) {
            std::vector<int> subQueue;
            subQueues.push_back(subQueue);
        }
        subQueues[timeUntilLeave].push_back(moneyAmount);
        if (timeUntilLeave > maxTimeUntilLeave) {
            maxTimeUntilLeave = timeUntilLeave;
        }
    }
    for (int i = 0; i < (int)subQueues.size(); i++) {
        sort(subQueues[i].begin(), subQueues[i].end());
    }
    int maximumMoney = 0;
    int numberPeopleToProcess = std::min(maxTimeUntilLeave+1, minutesUntilClosed);
    numberPeopleToProcess = std::min(numberPeopleToProcess, numPeopleInQueue);
    for (int i = numberPeopleToProcess-1; i >= 0; i--) {
        int queueIndex = (int)subQueues.size()-1;
        int bestChoice = subQueues[queueIndex].back();
        for (int j = queueIndex; j >= i; j--) {
            if (!subQueues[j].empty() && subQueues[j].back() > bestChoice) {
                bestChoice = subQueues[j].back();
                queueIndex = j;
            }
        }
        maximumMoney += bestChoice;
        subQueues[queueIndex].pop_back();
    }
    std::cout << maximumMoney << std::endl;
    return 0;
}