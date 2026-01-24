#include <bits/stdc++.h>
using namespace std;

void solve() {
    int nc;
    if (!(cin >> nc)) return;
    
    while (nc--) {
        string num;
        cin >> num;
        
        vector<int> roundNums;
        int powerOfTen = 1;

        for (int j = num.size() - 1; j >= 0; --j) {
            int digit = num[j] - '0'; 
            if (digit != 0) {
                roundNums.push_back(digit * powerOfTen);
            }
            powerOfTen *= 10;
        }
        cout << roundNums.size() << endl;
        for (int i = 0; i < roundNums.size(); ++i) {
            cout << roundNums[i] << (i == roundNums.size() - 1 ? "" : " ");
        }
        cout << endl;
    }
}

int main(){
    solve();
    return 0;
}
