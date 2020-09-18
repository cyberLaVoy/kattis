#include <iostream>

struct jewel {
	int size;
	int value;
};
void printRow(int* row, int size) {
	for (int i = 1; i < size; i++) {
		std::cout << row[i];
		std::cout << ' ';
	}
	std::cout << '\n';

}
void gatherJewelInfo(jewel* jewels, int numJewels) {
	jewel je;	
	for(int i = 0; i < numJewels; i++) {
		std::cin >> je.size;
		std::cin >> je.value;
		jewels[i] = je;
	}
}
void fillBaseCase(int* prevRow, int* currRow, int rowSize, jewel firstJewel) {
	for (int j = 0; j < rowSize; j++) {
		if (firstJewel.size <= j) {
			prevRow[j] = firstJewel.value;
		}
		else {
			prevRow[j] = 0;
		}
	}
	for (int j = 0; j < rowSize; j++) {
		currRow[j] = 0;
	}
}
void lastRowKnapsack(int numJewels, int maxCapacity, jewel* jewels) {
	int jewelSize, jewelValue;
	int bestWOItem, bestWithItem;
	int m = maxCapacity + 1; 
	int* prevRow = new int[m];
	int* currRow = new int[m];
	fillBaseCase(prevRow, currRow, m, jewels[0]);
	for (int i = 1; i < numJewels; i++) {
		jewelSize = jewels[i].size;
		jewelValue = jewels[i].value;
		for (int j = 1; j < m; j++) {
			bestWOItem = prevRow[j];
			if (jewelSize <= j) {
				bestWithItem = jewelValue + prevRow[j-jewelSize];
				currRow[j] = bestWithItem > bestWOItem ? bestWithItem : bestWOItem;
			}
			else {
				currRow[j] = bestWOItem;
			}
		}
		int* temp = currRow;
		currRow = prevRow;
		prevRow = temp;
	}
	printRow(prevRow, m);
	delete prevRow;
	delete currRow;
}

int main() {
	int numJewels;
	int maxCapacity;
	std::cin >> numJewels;	
	std::cin >> maxCapacity;	
	jewel* jewels = new jewel[numJewels];
	gatherJewelInfo(jewels, numJewels);
	lastRowKnapsack(numJewels, maxCapacity, jewels);
	delete jewels;
	return 0;
}
