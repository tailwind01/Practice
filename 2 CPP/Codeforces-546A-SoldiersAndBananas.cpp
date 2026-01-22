#include <bits/stdc++.h>
using namespace std;

// usage of arithmetic progression with common difference k
// to avoid problems with odd numbers in formula, we use floating point numbers in input
// we switch to integers only at output stage (since it will be an integer always)

void solve(){
    long double k,n,w;
    cin >> k >> n >> w;
    long double reqdAmt = w/2*(2*k+(w-1)*k);
    long double ownAmount = n;
    int ans = 0 ;
    if ((reqdAmt-ownAmount)>0){
        int borrowed = (reqdAmt-ownAmount);
        ans += borrowed;
    };
    cout << ans << endl;
}

int main(){
    solve();
    return 0;
}
