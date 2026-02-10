#include <bits/stdc++.h>
using namespace std;

void solve(){
    int price;
    cin >> price;
    int p10p = log10(price);
    int ans = price-pow(10,p10p);
    cout << ans << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
