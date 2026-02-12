#include <bits/stdc++.h>
using namespace std;

void solve(){
    int a,b,c,x,y;
    cin >> a >> b >> c >> x >> y;
    int cFc = max(x-a,0), dFc = max(y-b,0);
    string ans = (c-cFc-dFc)>=0 ? "Yes":"No";
    cout << ans << "\n";
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
