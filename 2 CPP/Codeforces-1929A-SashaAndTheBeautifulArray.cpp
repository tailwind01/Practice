#include <bits/stdc++.h>
using namespace std;

void solve(){
    int s;
    cin >> s;
    int first;
    cin >> first;
    s--;
    int maxelem = first, minelem = first;
    while(s--){
        int num;
        cin >> num;
        if (num<minelem){
            minelem = num;
        }
        if(num>maxelem){
            maxelem = num;
        }
    }
    cout << maxelem-minelem << "\n";
}

int main(){
    int nc;
    cin >> nc;
    while(nc--){
        solve();
    }
    return 0;
}
