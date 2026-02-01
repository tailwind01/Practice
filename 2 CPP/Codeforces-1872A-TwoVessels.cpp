#include <bits/stdc++.h>
using namespace std;

void solve(){
    int nc;
    cin >> nc;
    while(nc--){
        //we shall have to take the inputs as doubles for convenience in formulaic framing
        double a,b,c;
        cin >> a >> b >> c;
        double ans = abs(a-b)/(2*c);
        cout << ceil(ans) << "\n";
    }
}

int main(){
    solve();
    return 0;
}
