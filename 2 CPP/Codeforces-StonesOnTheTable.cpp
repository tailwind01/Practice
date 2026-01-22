#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    string stones;
    cin >> n;
    cin >> stones;
    int ans = 0;
    for (int i=0;i<n-1;++i){
        if (stones[i]==stones[i+1]){
            ans +=1 ;
        }
    }
    cout << ans << endl;
}

int main(){
    solve();
    return 0;
}
