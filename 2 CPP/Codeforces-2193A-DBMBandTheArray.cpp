#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,s,x;
    cin >> n >> s >> x;
    int currSum = 0;
    for(int i=0; i<n;++i){
        int num;
        cin >> num;
        currSum+=num;
    }
    string ans = (s>=currSum && (s-currSum)%x==0) ? "Yes":"No";
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
