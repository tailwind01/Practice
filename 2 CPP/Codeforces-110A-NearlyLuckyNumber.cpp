#include <bits/stdc++.h>
using namespace std;

void solve(){
    string n;
    cin >> n; 
    int luckycount = 0;
    string ans = "NO";
    for(int i=0;i<n.size();i++){
        if (n[i]=='4' or n[i]=='7'){
            luckycount+=1;
        }
    }
    if ((luckycount==4) or (luckycount==7)){
        ans = "YES";
    };
    
    cout << ans << endl; 
};

int main(){
    solve();
    return 0;
}
