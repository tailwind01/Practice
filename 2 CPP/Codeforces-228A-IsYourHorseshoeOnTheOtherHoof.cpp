#include <bits/stdc++.h>
using namespace std;

void solve(){
    vector <int> colors;
    for(int i=0;i<4;i++){
        int c;
        cin >> c;
        colors.push_back(c);
    };
    
    set <int> uniques (colors.begin(),colors.end());
    int ans = 4-uniques.size();
    cout << ans << endl;
};

int main(){
    solve();
    return 0;
};
