#include <bits/stdc++.h>
using namespace std;

void solve() {
    int k,r;
    cin >> k >> r;
    int numShovels = 0; 
    int outlay = 0; 
    for(int i=1;i<11;i++){
        if((outlay%10!=0 and outlay%10!=r) or numShovels==0){
            numShovels=i;
            outlay=i*k;
            }
        else{
            break;
            }
        }
    cout << numShovels << endl;
}

int main(){
    solve();
    return 0;
}
