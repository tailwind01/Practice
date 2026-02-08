#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int maxNum = 0;
    // we don't need to store the numbers, just the largest number..
    // this is so because we have the possibility of l==r, so we always output maxNum
    for(int i=0;i<n;++i){
        int num;
        cin >> num;
        if(num>maxNum){
            maxNum = num;
        }
    }
    cout << maxNum << "\n";
}

int main(){
    int nc;
    cin >> nc;
    while(nc--){
        solve();
    }
    return 0;
}
