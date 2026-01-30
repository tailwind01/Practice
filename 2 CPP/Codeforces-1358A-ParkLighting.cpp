#include <bits/stdc++.h>
using namespace std;

void solve(){
    int nc;
    cin >> nc;
    //greedy would be to cover as much as possible by middle lamp
    //so only if n*m is odd, would we need an extra lamp
    while(nc--){
        int n,m;
        cin >> n >> m;
        int ans = (n*m)/2;
        ans+=(n%2==1 and m%2==1) ? 1:0;
        cout << ans << "\n";
    }
}

int main(){
    solve();
    return 0;
}
