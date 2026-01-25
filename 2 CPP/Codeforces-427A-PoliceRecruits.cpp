#include <bits/stdc++.h>
using namespace std;

void solve() {
    int events;
    cin >> events;
    int activeforce = 0;
    int committedcrimes = 0;
    while(events--){
        int e;
        cin >> e;
        if(e>0){
            activeforce+=e; //recruits strengthen the active force
        }
        else{
            if(activeforce<abs(e)){
                committedcrimes+=abs(e); //no one was available to solve the crime
            }
            else{
                activeforce-=abs(e); //someone is available to solve the crime
            }
        }
    }
    cout << committedcrimes << endl;
}

int main(){
    solve();
    return 0;
}
