#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n ;
    string s1;
    cin >> s1;
    string lcase = "abcdefghijklmnopqrstuvwxyz";
    string upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string ans = "YES";
    for(int i=0;i<26;i++){
        auto count1 = count(s1.begin(),s1.end(),lcase[i]);
        auto count2 = count(s1.begin(),s1.end(),upcase[i]);
        if (count1==0 && count2==0){
            ans = "NO";
            break;
            };
    };
    cout << ans << endl;
};

int main(){
    solve();
    return 0;
};
