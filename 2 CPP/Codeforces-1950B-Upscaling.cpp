#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    
    string hashPattern = "##", dotPattern = "..";
    string firstRow="", thirdRow="";
    
    for(int i=0; i<2*n; i+=2){
        int iMultiple = i/2;
        if(iMultiple%2==0){
            firstRow.append(hashPattern);
            thirdRow.append(dotPattern);
        }
        else{
            firstRow.append(dotPattern);
            thirdRow.append(hashPattern);
        };
    };
    
    for(int j=0; j<2*n;++j){
        int jAsMultiple = j/2;
        if(jAsMultiple%2==0){
            cout << firstRow << endl;
        }
        else{
            cout << thirdRow << endl;
        };
    };
}

int main(){
    int nc;
    cin >> nc;
    
    for(int x = 0; x<nc; ++x){
        solve();
    };
    return 0;
}
