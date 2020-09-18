#include <iostream>
#include <string>
#include <algorithm>
#include <map>

void fillSubmissionsMap(int numSubs, std::map<std::string, int>& submissions) {
    std::string sub;
    for (int i = 0; i < numSubs; i++) {
       std::cin >> sub;
       if ( submissions.find(sub) == submissions.end() ) {
            submissions[sub] = 1;
       } 
       else {
            submissions[sub] += 1;
       }
    }
}

int main() {
    std::map<std::string, int> domSubmissionsCounts; 
    std::map<std::string, int> katSubmissionsCounts; 
    int numSubs;
    std::cin >> numSubs;
    fillSubmissionsMap(numSubs, domSubmissionsCounts);
    fillSubmissionsMap(numSubs, katSubmissionsCounts);
    int total = 0;
    std::map<std::string,int>::iterator it;
    for (it = domSubmissionsCounts.begin(); it != domSubmissionsCounts.end(); it++) {
        std::string key = it->first;
        int domCount = it->second;
        if (katSubmissionsCounts.find(key) != katSubmissionsCounts.end()) {
            int katCount = katSubmissionsCounts[key];
            total += std::min(domCount, katCount);
        }
    }
    std::cout << total << std::endl;
    return 0;
}