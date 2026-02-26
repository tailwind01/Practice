#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int second = (n%3==0)? n/3 : (n+3)/3;
    int first = second+1;
    int third = n-first-second;
    if(third==0){
        third++;
        second--;
    }
    cout << second << " " << first << " " << third << "\n";
}

int main(){
    int nc;
    cin >> nc;
    while(nc--){
        solve();
    }
    return 0;
}
