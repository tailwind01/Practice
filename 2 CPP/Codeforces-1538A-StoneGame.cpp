#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    // we don't need to store the numbers, just the positions of 1 and N..
    int l1,ln;
    for(int i=1;i<n+1;i++){
        int num;
        cin >> num;
        if(num==1){
            l1 = i;
        }
        if(num==n){
            ln = i;
        }
    }
    int r1 = n-l1+1, rn = n-ln+1;
    vector <int> possibs {max(l1,ln),max(r1,rn),l1+rn,r1+ln};
    sort(possibs.begin(),possibs.end());
    cout << possibs[0] << "\n";
}

int main(){
    int nc;
    cin >> nc;
    while(nc--){
        solve();
    }
    return 0;
}
