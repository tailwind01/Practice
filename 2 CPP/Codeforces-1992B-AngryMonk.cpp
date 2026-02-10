#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,k;
    cin >> n >> k;
    vector <int> pieces(k);
    copy_n(istream_iterator <int>(cin), k, pieces.begin());
    int ans = 2*(accumulate(pieces.begin(),pieces.end(),0)-*max_element(pieces.begin(),pieces.end())) - (k-1);
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
