#include <iostream>

int main() {
    int numTests;
    std::cin >> numTests;
    int l1,a1,l2,a2,lt,at;
    for (int i = 0; i < numTests; i++) {
        std::cin >> l1 >> a1 >> l2 >> a2 >> lt >> at;
        int solved = 0;
        int type1 = 0;
        int type2 = 0;
        int tempType1 = 1;
        while( tempType1 <= lt/l1 && solved <= 1 ) { // while type 1 count is <= the max possible l1 that divides into lt; and the probelm hasn't been solved more than once
            double tempType2 = (double)(lt - tempType1*l1) / (double)l2; // remainer of legs / number of legs for type2 = number of type 2 robots
                // at least on type 2 robot; and all arms accounted for; and numer of type 2 robots is an integer; and all legs accounted for
            if( tempType2 >= 1 && at-(tempType1*a1+tempType2*a2) == 0 && !(tempType2 > (int)tempType2) && lt-(tempType1*l1+tempType2*l2) == 0 ) { 
                type1 = tempType1;
                type2 = tempType2;
                solved++;
            }
            tempType1++; // try adding another type1 robot
        }
        if (solved != 1) {
            std::cout << '?' << std::endl;
        }
        else {
            std::cout << type1 << ' ' << type2 << std::endl;
        }
    }
    return 0;
}