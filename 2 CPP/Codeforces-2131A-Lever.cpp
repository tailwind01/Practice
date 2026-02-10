#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector <int> a(n);
    copy_n(istream_iterator<int>(cin),n,a.begin());
    vector <int> b(n);
    copy_n(istream_iterator<int>(cin),n,b.begin());
    int opers = 0;
    for(int i =0;i<n;++i){
        int diff = a[i]-b[i];
        if (diff>0){
            opers+=diff;
        }
    }
    cout << opers+1 << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
