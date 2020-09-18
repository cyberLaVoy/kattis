#include <iostream>

int numUniqueCds = 1000000001;
bool cds[1000000001] = { 0 }; // causes a stack overflow if in function (I think?)

int main() {
    int jackCdCount;
    int jillCdCount;
    std::cin >> jackCdCount;
    std::cin >> jillCdCount;

    while ( !(jackCdCount == 0 && jillCdCount == 0) ) {
        int cdId;
        int bothOwnCount = 0;
        int* resetIds;
        resetIds = new int[jackCdCount];
        for (int i = 0; i < jackCdCount; i++) {
            std::cin >> cdId;
            cds[cdId] = true;
            resetIds[i] = cdId;
        }
        for (int i = 0; i < jillCdCount; i++) { 
            std::cin >> cdId;
            if ( cds[cdId] ) {
                bothOwnCount++;
            }
        }
        std::cout << bothOwnCount << '\n';

        // reset cds
        for (int i = 0; i < jackCdCount; i++) {
            cds[resetIds[i]] = false;
        }
        delete[] resetIds;
    
    std::cin >> jackCdCount;
    std::cin >> jillCdCount;
    }
    return 0;
}