#include <iostream>
#include <vector>
#include <utility>
#include <iomanip> 

void determineWinLose(int p1, std::string m1, int p2, std::string m2, std::vector<std::pair<int, int>>& winLosePairs) {
    std::pair<int, int> winLose (-1,-1);
    if ( (m1 == "rock" && m2 == "scissors") || (m1 == "paper" && m2 == "rock") || (m1 == "scissors" && m2 == "paper") ) {
        winLosePairs[p1].first += 1;
        winLosePairs[p2].second += 1;
    }
    if ( (m2 == "rock" && m1 == "scissors") || (m2 == "paper" && m1 == "rock") || (m2 == "scissors" && m1 == "paper") ) {
        winLosePairs[p2].first += 1;
        winLosePairs[p1].second += 1;
    }
}
void displayOutcome(std::vector<std::pair<int, int>>& winLoseScores) {
    for (int i = 0; i < (int)winLoseScores.size(); i++) {
        if(winLoseScores[i].first + winLoseScores[i].second == 0) {
            std::cout << '-' << std::endl;
        }
        else {
            double winAverage = (double)winLoseScores[i].first/(double)(winLoseScores[i].first+winLoseScores[i].second);
            std::cout << std::fixed << std::setprecision(3) << (double)winAverage  << std::endl;
        }
    }
}
int main() {
    int numPlayers, k;
    while (std::cin >> numPlayers >> k) {
        int numGames = k*numPlayers*(numPlayers-1)/2; // this was the tricky part to consider
        std::vector<std::pair<int, int>> winLoseScores;
        for (int i = 0; i < numPlayers; i++) {
            std::pair<int, int> score(0, 0);
            winLoseScores.push_back(score);
        }
        std::string m1, m2;
        int p1, p2;
        for (int i = 0; i < numGames; i++) {
            std::cin >> p1 >> m1 >> p2 >> m2;
            p1--; p2--; // for consistent indexing
            determineWinLose(p1, m1, p2, m2, winLoseScores);
        }
        displayOutcome(winLoseScores);
        std::cout << std::endl;
    } 
    return 0;
}