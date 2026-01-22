#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    // let's try to be greedy and make alternating swaps
    int mod5 = n%5;
    int ans = n/5;
    if (mod5>0){
        ans+=1;
    };
    cout << ans << endl;
}

int main(){
    solve();
    return 0;
}
