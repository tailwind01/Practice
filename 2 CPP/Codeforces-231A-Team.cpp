#include <iostream>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int ans = 0;
    for (int i=0; i<n; ++i){
        int p,v,t;
        cin >> p >> v >> t;
        if (p+v+t>=2){
            ans+=1;
        };
    };
    cout << ans << endl;
}

int main(){
    solve();
}
