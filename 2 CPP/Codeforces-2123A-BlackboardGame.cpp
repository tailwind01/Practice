#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    string ans = (n%4==0) ? "Bob" : "Alice";
    cout << ans << "\n";
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
