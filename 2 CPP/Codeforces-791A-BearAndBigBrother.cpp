#include <bits/stdc++.h>
using namespace std;

void solve(){
    float l,b;
    cin >> l >> b;
    
    float currRatio = b/l;
    int numYrs = ceil(3*currRatio/2);
    int ans = 1 ;
    for(int i=0; i<numYrs; ++i){
        l = l*3;
        b = b*2;
        if (l>b){
            ans+=i;
            break;
        };
    };
    cout << ans << endl;
}

int main(){
    solve();
}
