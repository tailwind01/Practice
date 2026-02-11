#include <bits/stdc++.h>
using namespace std;

void solve(){
    string given;
    cin >> given;
    char s;
    cin >> s;
    int ansBool = 0;
    for(int i=0;i<given.size();++i){
        if (i%2==0 && given[i]==s){
            ansBool = 1;
            break;
        }
    }
    string ans = (ansBool==1) ? "Yes":"No";
    cout << ans << "\n";
}

int main(){
    int ncases;
    cin >> ncases;
    while(ncases--){
        solve();
    }
    return 0;
}
