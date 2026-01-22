#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n ;
    int available = 0; // initialized
    for (int i=0;i<n;++i){
        int p,q;
        cin >> p >> q;
        int spare=q-p;
        available+=(spare>=2);
    }
    
    cout << available << endl;
};

int main()
{
    solve();
    return 0;
}
