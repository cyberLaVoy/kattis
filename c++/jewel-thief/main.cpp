#include <iostream>
#include <vector>
#include <algorithm>

const int MAX_JEWEL_SIZE = 300;

class Curve {
    public:
        int a, b, t;
        long c;
        Curve() {
        }
        Curve(int aa, int bb, long cc) {
            a = aa; b = bb; c = cc;
        }
        long f(int x) {
            return x >= a ? 0 : sum[a-x-1]+c;
        }
        // Calculate earliest time this overtakes rhs
        int ot(Curve rhs) {
            int lo = b, hi = a-1;
            while (lo < hi) {
                int m = (lo+hi) / 2;
                if (f(m) >= rhs.f(m))
                    hi = m;
                else
                    lo = m+1;
            }
            return hi;
        }

        static std::vector<long> sum;
        static void updateSum(std::vector<int> values) {
            sum.clear();
            for (int i = 0; i < (int)values.size(); i++) {
                sum.push_back(values[i]);
            }
            for (int i = 0; i+1 < (int)sum.size(); i++) {
                sum[i+1] += sum[i];
            }
        }
};
std::vector<long> Curve::sum = {}; // instatiate static member variables

std::vector< std::vector<int> > gatherJewels(int numJewels) {
    std::vector< std::vector<int> > jewels;
    for (int s = 0; s <= MAX_JEWEL_SIZE; s++) {    // create bins for each unique jewel weight
        std::vector<int> values; 
        jewels.push_back(values);
    }
    for (int i = 0; i < numJewels; i++) {         // gather jewels info from input
        int size, value;
        std::cin >> size >> value;
        jewels[size].push_back(value);            // place jewel value into respective weight bin
    }
    for(int s = 0; s < (int)jewels.size(); s++) { // sort each weight bin in reverse order
        sort(jewels[s].rbegin(), jewels[s].rend());
    }
    return jewels;
}

void displayResult(std::vector<long>& dp, int K) {
    std::cout << dp[1];
    for (int i = 2; i <= K; i++) {
        std::cout << ' ' << dp[i];
    }
    std::cout << std::endl;
}


int main() {
    int numJewels, K; 
    std::cin >> numJewels >> K;
    std::vector< std::vector<int> > jewels = gatherJewels(numJewels);

    std::vector<long> dp(K+1);
    std::vector<Curve> dq(K+1);
    for (int s = 0; s < (int)jewels.size(); s++) if (jewels[s].size() > 0){
        Curve::updateSum(jewels[s]);
        // Update each congruence class
        // Runtime O(K log N)
        for (int m = 0; m < s; m++) {
            int start = K-m, j = 1, fptr = 0, bptr = 0;
            for (int i = 0; start-i*s >= 0; i++) {
                // Relax outdated
                while (bptr-fptr > 0 && dq[fptr].a <= i)
                    fptr++;
                while (j-i <= (int)jewels[s].size() && (start-j*s) >= 0) {
                    int pos = start-j*s;
                    Curve nc = Curve(j, i, dp[pos]);
                    if (fptr < bptr)
                        dq[bptr-1].t = nc.ot(dq[bptr-1]);
                    // Maintain deque invariant
                    while (bptr-fptr > 1 && dq[bptr-1].t <= dq[bptr-2].t) {
                        bptr--;
                        dq[bptr-1].t = nc.ot(dq[bptr-1]);
                    }
                    dq[bptr++] = nc;
                    j++;
                }
                // Relax overtaken
                while (bptr-fptr > 1 && dq[fptr].f(i) <= dq[fptr+1].f(i))
                    fptr++;
                // Update solution
                if (fptr < bptr) {
                    int pos = start-i*s;
                    dp[pos] = std::max(dp[pos], dq[fptr].f(i));
                }
            }
        }
    }

    displayResult(dp, K);

    return 0;
}