#include <bits/stdc++.h>
using namespace std;

//since the answer can be a floating number, we take inputs as 'double'

void solve(){
    double n;
    cin >> n;
    double totJuice = 0.00;
    for(int i=0;i<int(n);++i){
        float juice;
        cin >> juice;
        totJuice += juice;
    };
    
    double ans = totJuice/n;
    
    cout << setprecision(16);
    cout << ans << endl;
};

int main(){
    solve();
    return 0;
};
