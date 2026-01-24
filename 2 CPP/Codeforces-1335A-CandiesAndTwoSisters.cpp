#include <bits/stdc++.h>
using namespace std;

void solve(){
    int nc;
    cin >> nc;
    
    for (int i=0;i<nc;++i){
        int candies;
        cin >> candies;
        int ans = (candies%2==0) ? candies/2 - 1 : candies/2 ;
        cout << ans << endl;
        
    }
}

int main(){
    solve();
    return 0;
}
