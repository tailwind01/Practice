#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int m1ct = 0,zeroct = 0;
    while(n--){
        int num;
        cin >> num;
        if (num==-1){
            m1ct++;
        }
        if(num==0){
            zeroct++;
        }
    }
    int ans = (m1ct%2==0) ? zeroct : zeroct+2;
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
