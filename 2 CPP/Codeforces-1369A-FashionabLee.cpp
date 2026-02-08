#include <bits/stdc++.h>
using namespace std;

void solve(){
    long sides;
    cin >> sides;
    string ans = ((sides%2==0) && (sides/2)%2==0) ? "YES": "NO";
    cout << ans << "\n";
}

int main(){
    int nc;
    cin >> nc;
    while(nc--){
        solve();
    }
    return 0;
}
