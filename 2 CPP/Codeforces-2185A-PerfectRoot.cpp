#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    cout << n <<" ";
    n-=1;
    if (n>=1){
        while(n>1){
            cout << n << " ";
            n-=1;
        }
        cout << 1 << "\n";
    }
    else{
        cout << "\n";
    }
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
