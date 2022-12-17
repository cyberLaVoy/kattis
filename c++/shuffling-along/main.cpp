#include <iostream>
#include <string>

void fillDeck(int* deck, int deckSize) {
    for (int i = 0; i < deckSize; i++) {
        deck[i] = i;
    }
}
void displayDeck(int* deck, int deckSize) {
     for (int i = 0; i < deckSize; i++) {
        std::cout << deck[i] << ' ';
    }  
    std::cout << std::endl;
}
bool isSorted(int* deck, int deckSize) {
    for(int i = 0; i < deckSize; i++) {
        if (deck[i] != i) {
            return false;
        }
    } 
    return true;
}
void splitDeck(int* deck, int* firstHalf, int* secondHalf, int firstHalfSize, int secondHalfSize) {
    for (int i = 0; i < firstHalfSize; i++) {
        firstHalf[i] = deck[i];
    }
    for (int i = 0; i < secondHalfSize; i++) {
        secondHalf[i] = deck[i+firstHalfSize];
    }
}
void shuffleIn(int* deck, int* firstHalf, int* secondHalf, int deckSize, int firstHalfSize, int secondHalfSize) {
    splitDeck(deck, firstHalf, secondHalf, firstHalfSize, secondHalfSize);
    for (int i = 0; i < firstHalfSize; i++) {
        deck[i*2+1] = firstHalf[i];
    }
    for (int i = 0; i < secondHalfSize; i++) {
        deck[i*2] = secondHalf[i];
    }
}
void shuffleOut(int* deck, int* firstHalf, int* secondHalf, int deckSize, int firstHalfSize, int secondHalfSize) {
    splitDeck(deck, firstHalf, secondHalf, firstHalfSize, secondHalfSize);
    for (int i = 0; i < firstHalfSize; i++) {
        deck[i*2] = firstHalf[i];
    }
    for (int i = 0; i < secondHalfSize; i++) {
        deck[i*2+1] = secondHalf[i];
    }
}
void setHalfSizes(int deckSize, int& firstHalfSize, int& secondHalfSize, std::string& type) {
    firstHalfSize = deckSize/2;
    secondHalfSize = deckSize/2;
    if (deckSize & 1 == 1) {
        if(type == "out") {
            firstHalfSize++;
        }
        else {
            secondHalfSize++;
        }
    }
}
int main() {
    int deckSize, firstHalfSize, secondHalfSize;
    std::string type;
    std::cin >> deckSize >> type;
    setHalfSizes(deckSize, firstHalfSize, secondHalfSize, type);
    int* deck = new int[deckSize];
    int* firstHalf = new int[firstHalfSize];
    int* secondHalf = new int[secondHalfSize];
    fillDeck(deck, deckSize);
    int numShuffles = 0;
    do {
        if (type == "out") {
            shuffleOut(deck, firstHalf, secondHalf, deckSize, firstHalfSize, secondHalfSize);
        }
        else {
            shuffleIn(deck, firstHalf, secondHalf, deckSize, firstHalfSize, secondHalfSize);
        }
        numShuffles++;
    }
    while (!isSorted(deck, deckSize));
    std::cout << numShuffles << std::endl;
    delete deck;
    delete firstHalf;
    delete secondHalf;

    return 0;
}