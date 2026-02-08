#include <bits/stdc++.h>
using namespace std;

void solve(){
    long a,b;
    cin >> a >> b;
    long ans = (a==0) ? 1: (a+b*2+1);
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
