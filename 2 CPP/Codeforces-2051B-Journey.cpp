#include <bits/stdc++.h>
using namespace std;
using lli = long long int;

void solve(){
    lli n,a,b,c;
    cin >> n >> a >> b >> c;
    lli fullCycles = n/(a+b+c);
    lli lastChunk = n%(a+b+c);
    lli days = fullCycles * 3;
    int iternum = 1;
    while(lastChunk>0){
        if(iternum ==1){
            lastChunk-=a;
            days +=1;
        }
        else if (iternum==2){
            lastChunk-=b;
            days+=1;
        }
        else{
            lastChunk-=c;
            days+=1;
        }
        iternum++;
    }
    cout << days << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
