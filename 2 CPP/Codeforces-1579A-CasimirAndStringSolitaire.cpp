#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t;
    cin >> t;
    while (t--){
        string s;
        cin >> s;
        int runningSum = 0 ;
        for(char &c:s){
            runningSum+=(c=='B')?-1:1;
        }
        string ans = (runningSum==0)? "YES":"NO";
        cout << ans << "\n";
    }
}

int main(){
    solve();
    return 0;
}
