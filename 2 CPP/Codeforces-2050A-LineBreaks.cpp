#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,m;
    cin >> n >> m;
    int firstSpace = m, accomodated = 0;
    while(n--){
        string word;
        cin >> word;
        int size = word.size();
        firstSpace-=size;
        accomodated+= (firstSpace>=0);
    }
    cout << accomodated << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
