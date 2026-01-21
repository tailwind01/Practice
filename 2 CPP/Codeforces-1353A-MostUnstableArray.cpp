#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m;
    cin >> n >> m;
    
    int ans = 0; //default for n==1
    
    if (n==2){
        ans = m;
    }
    else if (n>2){
        ans = 2*m;
    };
    
    cout << ans << endl;
}

int main(){
    int nc;
    cin >> nc;
    for (int j=0; j<nc;++j){
        solve();
    };
}
