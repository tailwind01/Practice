//first code on my birthday, so happy birthday to me :24/01/2026 :D
#include <bits/stdc++.h>
using namespace std;
using ll=long long;

void solve(){
    int n;
    cin >> n ;
    
    for(int i=0;i<n;++i){
        ll a, b;
        cin >> a >> b ;
        ll ans = (a%b==0) ? 0:b-(a%b); // using the ternary operator idiom
        cout << ans << endl;
    }
    
};

int main(){
    solve();
    return 0;
};
