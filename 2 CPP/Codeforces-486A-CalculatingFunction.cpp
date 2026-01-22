#include <bits/stdc++.h>
using namespace std;
using lli = long long int;

void solve(){
    lli n;
    cin >> n ;
    lli ans = (n%2==0) ? n/2 : (-1)*(n+1)/2;
    
    cout << ans << endl;
};

int main()
{
    solve();
    return 0;
}
