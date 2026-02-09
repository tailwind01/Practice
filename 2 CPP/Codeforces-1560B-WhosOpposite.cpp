#include <bits/stdc++.h>
using namespace std;
using l2 = long;

void solve(){
    l2 a,b,c;
    cin >> a >> b >> c;
    l2 diff = abs(b-a);
    l2 ceiling = 2*diff;
    l2 ans;
    if(a>ceiling || b> ceiling || c>ceiling || diff==1 ){
        ans = -1;
    }
    else{
        ans = ((c+diff)>ceiling) ? c-diff : c+diff;
    }
    cout << ans << "\n";
}

int main(){
    l2 tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
