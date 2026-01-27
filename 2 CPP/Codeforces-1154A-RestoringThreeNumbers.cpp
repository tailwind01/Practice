#include <bits/stdc++.h>
using namespace std;

void solve() {
    int a,b,c,d;
    cin >> a >> b >> c >> d;
    vector <int> all = {a,b,c,d};
    sort(all.begin(),all.end());
    vector <int> diffing;
    for (int i=0;i<3;i++){
        int diff = all[3]-all[i]; //basically (a+b+c)-(a+b)=c convention
        diffing.push_back(diff);
    }
    
    cout << diffing[0]<< " "<<diffing[1]<<" "<< diffing[2] << endl;
    
}

int main(){
    solve();
    return 0;
}
