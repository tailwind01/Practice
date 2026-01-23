#include <bits/stdc++.h>
using namespace std;

void solve(){
    int levels;
    cin >> levels ;
    int p;
    cin >> p;
    vector <int> passes;
    for(int i=0;i<p;i++){
        int lp;
        cin >> lp;
        passes.push_back(lp);
    };
    
    int q;
    cin >> q;
    for(int j=0;j<q;j++){
        int lq;
        cin >> lq;
        passes.push_back(lq);
    };
    
    set <int> uniques (passes.begin(),passes.end());
    
    string ans = (uniques.size()==levels) ? "I become the guy.":"Oh, my keyboard!"; // using the ternary for awesomeness!
    
    cout << ans << endl;
};

int main(){
    solve();
    return 0;
};
