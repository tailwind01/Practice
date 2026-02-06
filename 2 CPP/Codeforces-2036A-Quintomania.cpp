#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    int isperfect = 1;
    int note;
    cin >> note;
    n= n-1;
    while(n--){
        int new_note;
        cin >> new_note;
        if(abs(new_note-note)!=5 and abs(new_note-note)!=7){
            isperfect = 0;
        }
        note = new_note;
    }
    string ans = (isperfect==1) ? "YES":"NO";
    cout << ans << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
