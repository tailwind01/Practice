#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t;
    cin >> t;
    while(t--){
        int len;
        cin >> len;
        int firstNum;
        cin >> firstNum;
        len -= 1;
        int prevModulo = firstNum%2;
        int corrections = 0;
        while(len--){
            int sieveNum;
            cin >> sieveNum;
            int currModulo = sieveNum%2;
            corrections += (currModulo==prevModulo);
            prevModulo = currModulo;
        }
        cout << corrections << "\n";
    }
}

int main(){
    solve();
    return 0;
}
