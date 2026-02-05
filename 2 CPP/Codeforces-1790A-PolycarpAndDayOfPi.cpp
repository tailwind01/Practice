#include <bits/stdc++.h>
using namespace std;

void solve(){
    string n;
    cin >> n;
    string base = "314159265358979323846264338327";
    int commons = 0;
    for(int i=0;i<n.size();i++){
        if (n[i]==base[i]){
            commons+=1;
        }
        else{
            break;
        }
    }
    cout << commons << "\n";
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
