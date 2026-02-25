#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int m7 = n%7;
    int ans = (n/10)==(n-m7)/10 ? n-m7 : n+7-m7;
    cout << ans << "\n";
}

int main(){
    int numcases;
    cin >> numcases;
    while (numcases--){
        solve();
    }
    return 0;
}
