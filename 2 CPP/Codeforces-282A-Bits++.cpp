#include <iostream>
#include <string>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int ans = 0;
    for (int i=0; i<n; ++i){
        string p;
        cin >> p;
        if (p.contains("+")){
            ans+=1;
        }
        else{
            ans-=1;
        };
    };
    cout << ans << endl;
}


int main(){
    solve();
}
