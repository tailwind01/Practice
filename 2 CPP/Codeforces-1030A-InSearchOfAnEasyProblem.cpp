#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n ;
    string ans = "Easy"; //initialized..
    //lets calculate the answer at the input stage itself
    for(int i=0;i<n;++i){
        int d;
        cin >> d;
        if(d==1){
            ans = "Hard";
            break;
        }
    }
    cout << ans << endl; 
};

int main(){
    ios_base::sync_with_stdio (false);
    solve();
    return 0;
}
