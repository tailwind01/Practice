#include <bits/stdc++.h>
using namespace std;
using lli = long long int;
void solve(){
    lli n;
    cin >> n;
    lli cumsum = 0;
    while(n>0){
        cumsum+=n;
        n=n/2;
    }
    cout << cumsum << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
