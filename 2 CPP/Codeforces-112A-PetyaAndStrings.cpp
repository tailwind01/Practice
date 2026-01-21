#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s1, s2;
    cin >> s1 ;
    cin >> s2;
    
    //before comparison of the strings we convert both of the inputs to lowercase
    // in order to ensure consistency in result
    
    for (char &c : s1){
        c = tolower(c); 
    };
    
    for (char &d : s2){
        d = tolower(d);
    };
    
    int ans = 0;
    
    if (s1>s2){
        ans = 1;
    }
    
    else if(s1<s2){
        ans = -1;
    };
    
    cout << ans << endl;
}

int main(){
    solve();
}
