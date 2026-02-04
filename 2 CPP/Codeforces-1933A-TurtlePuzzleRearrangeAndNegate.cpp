#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int runningsum = 0;
        while(n--){
            int x;
            cin >> x;
            runningsum+=abs(x);
        }
        cout << runningsum << "\n";
    }
}

int main(){
    solve();
    return 0;
}
