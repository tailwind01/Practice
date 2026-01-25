#include <bits/stdc++.h>
using namespace std;

void solve() {
    string a,b,c;
    cin >> a ;
    cin >> b ;
    cin >> c ;
    string totString = a+b;
    sort(c.begin(),c.end());
    sort(totString.begin(),totString.end());
    string ans;
    ans = (c==totString) ? "YES" :"NO";
    cout << ans << endl;
}

int main(){
    solve();
    return 0;
}
