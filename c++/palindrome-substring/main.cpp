#include <iostream>
#include <string>
#include <vector>
#include <set>

void printPalindromeSubstrings(std::string str) {
    std::set<std::string> palindromes;
    int n = str.size();
    std::vector<std::vector<bool>> L(n, std::vector<bool>(n));
    for (int i = 0; i < n; i++)
        L[i][i] = true;
    for (int gap = 1; gap < n; gap++) {
        for (int row = 0; row < n-gap; row++) {
            int col = row + gap; 
            if (str[row] == str[col] && gap == 1) { // size 2 palindromes
                L[row][col] = true;
                palindromes.insert(str.substr(row, col-row+1));
            }
            else if (str[row] == str[col] && L[row+1][col-1]) { // size > 2 palindromes
                L[row][col] = true;
                palindromes.insert(str.substr(row, col-row+1));
            }
        }
    }
    for (std::set<std::string>::iterator it = palindromes.begin(); it != palindromes.end(); it++) {
        std::cout << *it << std::endl;
    }
}
int main() {
    std::string fullString;
    while (std::cin >> fullString) {
        printPalindromeSubstrings(fullString);
    }
    return 0;
}