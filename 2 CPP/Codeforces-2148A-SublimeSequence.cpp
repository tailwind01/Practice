#include <bits/stdc++.h>
using namespace std;

void solve(){
    int x,n;
    cin >> x >> n ;
    int ans = x;
    if(n%2==0){
        ans = 0;
    }
    cout << ans << endl;
}

int main(){
    int nc;
    cin >> nc;
    
    for(int i=0; i<nc;++i){
        solve();
    };
    
    return 0;
}
