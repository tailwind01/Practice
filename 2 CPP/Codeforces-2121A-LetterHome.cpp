#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,s;
    cin >> n >> s;
    vector <int> positions;
    for(int i=0;i<n;i++){
        int num;
        cin >> num;
        positions.push_back(num);
    };
    int begin = positions[0], end = positions[n-1];
    int moves;
    if(s<begin){
        moves = end-s;
    }
    else if(s>end){
        moves = s-begin;
    }
    else{
        moves = min(abs(s-begin),abs(s-end))+end-begin;
    };
    cout << moves << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
