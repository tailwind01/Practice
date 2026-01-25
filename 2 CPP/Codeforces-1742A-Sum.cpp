#include <bits/stdc++.h>
using namespace std;

void solve() {
    int nc;
    if (!(cin >> nc)) return;
    
    while (nc--) {
        int a,b,c;
        cin >> a >> b >> c;
        double total = a+b+c;
        string ans;
        ans = (total/2==a || total/2==b || total/2==c) ? "YES" :"NO";
        cout << ans << endl;
    }
}

int main(){
    solve();
    return 0;
}
