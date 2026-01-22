#include <bits/stdc++.h>
using namespace std;

void solve(){
    long long n,s;
    cin >> n >> s ; 
    long long ans = n;
    for(int i=0;i<s;++i){
        if (ans%10==0){
            ans = ans/10;
        }
        else{
            ans-=1;
        };
    };
    
    cout << ans << endl;
}

int main(){
    solve();
    return 0;
}
