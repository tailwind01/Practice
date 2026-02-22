#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int maxNum = 0;
    // we dont need to store the entire input array, it will be fluff
    for(int i=0;i<n;++i){
        int num;
        cin >> num;
        if (num>maxNum){
            maxNum = num;
        }
    }
    cout << n*maxNum << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
