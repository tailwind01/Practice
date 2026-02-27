#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    string original, target;
    cin >> original >> target;
    int moves = 0;
    for(int i=0;i<n;++i){
        int o = original[i]-'0';
        int t = target[i]-'0';
        moves += min(abs(o-t),10-abs(o-t));
    }
    cout << moves << "\n";
}
