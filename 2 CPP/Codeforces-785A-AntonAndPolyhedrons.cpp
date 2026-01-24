#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int lookup[128]={0};
    lookup['T'] = 4;
    lookup['C'] = 6;
    lookup['O'] = 8;
    lookup['D'] = 12;
    lookup['I'] = 20;
    
    int ans = 0;
    string shape;
    for(int i=0;i<n;++i){
            cin >> shape;
            ans+= lookup[shape[0]];
    };
    
    cout << ans << endl;
};

int main(){
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
};
