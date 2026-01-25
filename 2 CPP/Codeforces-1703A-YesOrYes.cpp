#include <bits/stdc++.h>
using namespace std;

void solve() {
    int tcases;
    cin >> tcases;
    while(tcases--){
        string inp;
        cin >> inp;
        string lcase;
        
        for(char &c:inp){
            lcase+=tolower(c);
        };
        
        string ans = (lcase=="yes") ? "YES":"NO";
        cout << ans << endl;
    }
}

int main(){
    solve();
    return 0;
}
