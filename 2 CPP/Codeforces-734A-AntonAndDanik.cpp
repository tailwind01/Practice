#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    string p;
    cin >> p; 
    int anton = 0, danik = 0;
    
    for(char &c: p){
        if (c=='A'){
            anton+=1;
        }
        else{
            danik+=1;
        };
    }
    
    string ans = "Friendship"; //let's initialize with the neutrality of outcomes, which changes if strict gt/lt
    
    if (anton>danik){
        ans = "Anton";
    }
    else if(danik>anton) {
        ans = "Danik";
    };
    
    cout << ans << endl; 
};

int main(){
    solve();
    return 0;
}
