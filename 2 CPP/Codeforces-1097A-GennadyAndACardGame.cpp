#include <bits/stdc++.h>
using namespace std;

void solve(){
    string tableCard;
    cin >> tableCard;
    char tcNum = tableCard[0];
    char tcClass = tableCard[1];
    int flag = 0;
    for(int i=0;i<5;++i){
        string dealtCard;
        cin >> dealtCard;
        if(dealtCard[0]==tcNum or dealtCard[1]==tcClass){
            flag=1;
            break;
        }
    }
    string ans = (flag==1)?"YES":"NO";
    cout << ans << "\n";
}

int main(){
    solve();
    return 0;
}
