#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,m;
    cin >> n >> m;
    string evenPattern (m,'#');
    string oddPattern1 = string(m-1,'.')+'#';
    string oddPattern2 = '#'+string(m-1,'.');
    
    for (int i=0;i<n;++i){
        if (i%2==0){
            cout << evenPattern << endl;
        }
        else if ((i-1)%4==0){
            cout << oddPattern1 << endl;
        }
        else{
            cout << oddPattern2 << endl;
        };
    }
}

int main(){
    solve();
    return 0;
}
