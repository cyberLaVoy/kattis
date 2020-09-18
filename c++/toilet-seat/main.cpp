#include <iostream>
#include <string>

void setLeaveState(bool* ruleState, int rule) {
    if (rule == 0) {
        *ruleState = false;
    }
    else if (rule == 1) {
        *ruleState = true;
    }
}
int calculateAdjustments(bool* sequence, int length, int rule) {
    bool leaveState = false;
    setLeaveState(&leaveState, rule);
    int totalAdjustments = 0;
    bool state = sequence[0];
    for (int i = 1; i < length; i++) {
        if (sequence[i] != state) {
            state = !state;
            totalAdjustments++;
        }
        if (rule != -1) {
            if (state != leaveState) {
                state = leaveState;
                totalAdjustments++;
            } 
        }
    }
    return totalAdjustments;
}
int main() {
    std::string sequence; 
    std::cin >> sequence;
    bool flips[sequence.length()] = { 0 };
    for (int i = 0; i < (int)sequence.length(); i++) {
        if (sequence[i] == 'U') {
            flips[i] = true;
        }
    }
    std::cout << calculateAdjustments(flips, sequence.length(), 1) << std::endl;
    std::cout << calculateAdjustments(flips, sequence.length(), 0) << std::endl;
    std::cout << calculateAdjustments(flips, sequence.length(), -1) << std::endl;
    return 0;
}