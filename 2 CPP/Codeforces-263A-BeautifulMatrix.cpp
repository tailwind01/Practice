#include <iostream>
using namespace std;

void solve(){
    int row = 0, col = 0;
    for (int i=0; i<25; ++i){
        int n;
        cin >> n;
        if (n==1){
            row=i/5 + 1;
            col = i%5 + 1;
        };
        
    };
    
    int ans = abs(row-3)+abs(col-3);
    
    cout << ans;
}


int main(){
    solve();
}
