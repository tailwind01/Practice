#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s;
    cin >> s ;
    int uc=0, lc=0;
    for (char &c:s){
        if (isupper(c)){
            uc+=1;
        }
        else{
            lc+=1;
        };
    };
    
    string ans = "";
    if (uc>lc){
        for (char &d: s){
            ans+=toupper(d);
        }
    }
    else{
        for (char &d: s){
            ans+=tolower(d);
        }
    };
    
    cout << ans << endl;
}

int main(){
    solve();
    return 0;
}
