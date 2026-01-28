//we needn't concern ourselves with the origin,
//we only need 3 conditions: l==r, u==d and l==u (horizontal match, vertical match, vertical & horizontal match)
//v2
//
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int tc;
    cin >> tc;
    
    while(tc--){
        int l,r,u,d;
        cin >> l >> r >> u >> d;
        string ans = (l==r && l==u && u==d) ? "YES":"NO";
        cout << ans << "\n";
    }
}

int main(){
    solve();
    return 0;
}



//v1
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int tc;
    cin >> tc;
    
    while(tc--){
        int l,r,u,d;
        cin >> l >> r >> u >> d;
        int horiz = l-r;
        int vert = u-d;
        string ans = (horiz==0 && vert == 0 && l==u) ? "YES":"NO";
        cout << ans << "\n";
    }
}

int main(){
    solve();
    return 0;
}
