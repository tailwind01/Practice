#include <bits/stdc++.h>
using namespace std;

void solve(){
    int m,a,b,c;
    cin >> m >> a >> b >> c ;
    int row1 = min(a,m),row2 = min(b,m),remaining=min(2*m-row1-row2,c);
    int ans = row1+row2+remaining;
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
