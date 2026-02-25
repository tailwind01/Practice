#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int ans = (n%2)== 0 ? 1 : 0; //the config in which no cow or no chick is present

    //another block to take cows config from 0 to int(n/4)
    if(n%2==0){
        ans += n/4 ;
    } 

    cout << ans << "\n";
}

int main(){
    int numcases;
    cin >> numcases;
    while (numcases--){
        solve();
    }
    return 0;
}
