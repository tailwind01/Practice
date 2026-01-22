#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s1;
    cin >> s1;
    string s2;
    cin >> s2;
    
    reverse(s1.begin(),s1.end());
    
    string ans = "YES"; //let's initialize with Yes, which changes if condition fails
    
    if (s2!=s1){
        ans = "NO";
    };
    
    cout << ans << endl; 
};

int main(){
    solve();
    return 0;
}
