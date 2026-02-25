#include <bits/stdc++.h>
using namespace std;

int main(){
    int nc;
    cin >> nc;
    while(nc--){
        int n;
        cin >> n;
        int ans = (n+2)/3;
        ans+= (n==1);
        cout << ans << "\n";
    }
    return 0;
}
