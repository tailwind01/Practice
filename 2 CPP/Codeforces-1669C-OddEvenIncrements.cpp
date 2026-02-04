#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector <int> modArr;
    for(int i=0;i<n;i++){
        int num;
        cin >> num;
        modArr.push_back(num%2);
    }
    set <int> sModArr (modArr.begin(),modArr.end());
    int ctr = 1; //assume that we have the solution until we see evidence to the contrary
    if(sModArr.size()>1){
        for(int j=1;j<n;j++){
            if(modArr[j]==modArr[j-1]){
                ctr = 0;
                break ;
            }
        }
    }
    string ans = (ctr==1) ? "YES" : "NO";
    
    cout << ans << "\n";
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
