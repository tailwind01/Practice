#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t;
    cin >> t;
    
    while(t--){
        int x;
        cin >> x;
        int log10x = log10(x);
        int nearestM = x/pow(10,log10x);
        int ans = 0;
        if(x<10){
            ans = x;
        }
        else{
            ans = log10x*9 + nearestM;
        }
        cout << ans << "\n";
    }
}

int main(){
    solve();
    return 0;
}
