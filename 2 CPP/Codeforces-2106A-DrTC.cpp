#include <bits/stdc++.h>
using namespace std;

void solve(){
    int size;
    cin >> size;
    string binaryrep;
    cin >> binaryrep;
    int ctof1s=0;
    for(int i=0;i<binaryrep.size();++i){
        ctof1s+=binaryrep[i]=='1';
    }
    int ctof0s = size-ctof1s;
    int ans = (size-1)*ctof1s+ctof0s;
    cout << ans << "\n";
}

int main(){
    int numcases;
    cin >> numcases;
    while(numcases--){
        solve();
    }
    return 0;
}
