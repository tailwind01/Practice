#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,x;
    cin >> n >> x;
    int first1=0, last1=0;
    for(int i=0;i<n;++i){
        int door;
        cin >> door;
        if (door==1 && first1==0){
            first1 = i+1;
        }
        if(door==1){
            last1 = i+1;
        }
    }
    string ans = (last1-first1)<x ? "Yes":"No";
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
