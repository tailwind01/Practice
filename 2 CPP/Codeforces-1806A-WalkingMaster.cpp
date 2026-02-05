#include <bits/stdc++.h>
using namespace std;

void solve(){
    long a,b,c,d;
    cin >> a >> b >> c >> d;
    long vert = d-b, horiz = c-a;
    long ans = (horiz>vert || vert<0) ? -1:2*vert-horiz;
    cout << ans << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
