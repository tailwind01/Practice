#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t;
    cin >> t;
    while(t--){
        int n,k;
        cin >> n >> k;
        string istr;
        cin >> istr;
        int ops = 0, ptr=0;
        while(ptr<n){
            if(istr[ptr]=='B'){
                ops+=1;
                ptr+=k;
            }
            else{
                ptr+=1;
            }
        }
        cout << ops << "\n";
    }
}

int main(){
    solve();
    return 0;
}
