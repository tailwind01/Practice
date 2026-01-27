#include <bits/stdc++.h>
using namespace std;

void solve() {
    int games;
    cin >> games ;
    // the crux of the code is if the number is divisible by 3
    // because if not, then the first player will win
    // and if it is, then the first player would never, ever win
    while(games--){
        int num;
        cin >> num;
        string ans = (num%3==0) ? "Second": "First";
        cout << ans << endl;
    }
    
}

int main(){
    solve();
    return 0;
}
