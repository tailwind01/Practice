#include <bits/stdc++.h>
using namespace std;

void solve() {
    int p, ttp;
    cin >> p >> ttp ;
    int needToLeave = 240-ttp; //this timer will get dynamically updated
    int solved = 0; //this counter will get dynamically updated
    int timeSpent = 0; // this will get updated
    for(int i=1;i<p+1;i++){
        int solveTime = i*5;
        if (needToLeave>=solveTime){ //essentially checking if we have time to solve one more
            needToLeave-=solveTime;
            timeSpent+=solveTime;
            solved+=1;
        }
        else{
            break; //we get the f out of the loop!
        };
    };
    cout << solved << endl;
}

int main(){
    solve();
    return 0;
}
