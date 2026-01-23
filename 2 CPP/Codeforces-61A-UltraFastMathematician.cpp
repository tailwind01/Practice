#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s1,s2;
    cin >> s1;
    cin >> s2;
    string ans ="";
    
    for(int i=0;i<s1.size();++i){
        string currNum;
        currNum = (s1[i]!=s2[i]) ? '1':'0'; // using the ternary operator idiom
        ans+=currNum;
    }
    
    cout << ans << endl;
    
    
};

int main(){
    solve();
    return 0;
};
