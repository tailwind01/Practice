#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t;
    cin >> t;
    while(t--){
        double yr;
        cin >> yr;
        double Sqroot = sqrt(yr);
        int int_sqroot = int(Sqroot);
        if (Sqroot==int_sqroot){
            cout << int_sqroot << " " << 0 << "\n";
        }
        else{
            cout << -1 << "\n";
        }
    }
}

int main(){
    solve();
    return 0;
}
