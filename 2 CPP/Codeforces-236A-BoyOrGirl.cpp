#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s1;
    cin >> s1;
    
    unordered_set <char> unique_chars(s1.begin(), s1.end());
    
    int size = unique_chars.size();
    
    //our output to be printed itself is conditional, so no use of setting up flags
    
    if (size%2==0){
        cout << "CHAT WITH HER!" << endl;
    }
    else{
        cout << "IGNORE HIM!" << endl;
    }
}

int main(){
    solve();
}
