#include <bits/stdc++.h>
using namespace std;

void solve(){
    int nc;
    cin >> nc;
    //our endeavor will be to process the input as it comes
    //we shall ensure equality by setting the ceiling to be n+1
    while(nc--){
        int n;
        cin >> n;
        for(int i=0;i<n-1;i++){
            int lc;
            cin >> lc;
            cout << n+1-lc << " ";
        }
        int lastNum;
        cin >> lastNum;
        cout << n+1-lastNum << "\n";
    }
}

int main(){
    solve();
    return 0;
}
