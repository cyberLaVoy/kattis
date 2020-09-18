#include <iostream>
#include <string>
#include <vector>

int countDoubleVowels(std::string word) {
    std::vector<std::string> doubleVowels = {"aa", "ee", "ii", "oo", "uu", "yy"};
    int doubleCount = 0;
    for (int i = 0; i < (int)doubleVowels.size(); i++) {
        int startPosition = 0;
        std::size_t foundPostion = word.find(doubleVowels[i], startPosition);
        while (foundPostion != std::string::npos) {
            doubleCount++;
            startPosition = foundPostion+2;
            foundPostion = word.find(doubleVowels[i], startPosition);
        }
    }
    return doubleCount;
}
std::string findBestWord(int numWords) {
    std::string word;
    std::string bestWord;
    int maxCount = -1; // guarantees that there will be a word to return
    for (int i = 0; i < numWords; i++) {
        std::cin >> word;
        int count = countDoubleVowels(word);
        if (count > maxCount) {
            bestWord = word;
            maxCount = count;
        }
    }
    return bestWord;
}
int main() {
    int numWords;
    std::cin >> numWords;
    while (numWords != 0) {
        std::cout << findBestWord(numWords) << std::endl; 
        std::cin >> numWords;
    }
    return 0;
}