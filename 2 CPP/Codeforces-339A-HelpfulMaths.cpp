#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s1;
    cin >> s1;
    string ph = s1;
    sort(ph.begin(),ph.end());
    erase(ph, '+');
    string ans ="";
    for (int i=0;i<ph.size()-1; i++)
    {
        ans.push_back(ph[i]);
        ans.push_back('+');
    };
    
    ans.push_back(ph[ph.size()-1]);
    
    cout << ans << endl;
}

int main(){
    solve();
}
