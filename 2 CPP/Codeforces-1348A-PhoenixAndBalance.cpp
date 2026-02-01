#include <bits/stdc++.h>
using namespace std;

void solve(){
    int nc;
    cin >> nc;
    while(nc--){
        int n;
        cin >> n;
        int ans = pow(2,n/2 + 1)-2;
        cout << ans << "\n";
    }
}

int main(){
    solve();
    return 0;
}
