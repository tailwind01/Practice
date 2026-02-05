#include <bits/stdc++.h>
using namespace std;

int main(){
    int l;
    cin >> l;
    string s;
    cin >> s;
    int ans = 0;
    for (int i = 2; i<l;i++){
        if(s[i]=='x' && s[i]==s[i-1] && s[i]==s[i-2]){
            ans+=1;
        };
    }
    cout << ans << "\n";
    return 0;
}
