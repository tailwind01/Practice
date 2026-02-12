#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    string init, finish;
    cin >> init >> finish;
    int days = 0, i1 = 0, f1= 0 ;
    for(int i=0; i<n;i++){
        char in = init[i], fin = finish[i];
        if(in=='1'){
            i1+=1;
        }
        if(fin=='1'){
            f1+=1;
        }
        if(in=='0' && fin =='1'){
            days+=1;
        }
    }
    int ans = days - min(f1-i1,0); // to adjust if we had a surplus in initial after finishing
    cout << ans << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
