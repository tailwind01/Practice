#include <bits/stdc++.h>
using namespace std;

void solve() {
    int runs;
    cin >> runs ;
    int minScore = 0 ,maxScore = 0;
    int s1;
    cin >> s1 ;
    minScore = s1; maxScore = s1; // initialized with max and min to be the same first entry
    int amazingTurns=0;
    for(int i=0;i<runs-1;i++){
        int score;
        cin >> score;
        amazingTurns += (maxScore<score) ? 1:0; //if either of these 2 conditions is true..
        amazingTurns += (minScore>score) ? 1:0; //if either of these 2 conditions is true..
        maxScore = (maxScore<score) ? score : maxScore; //resetting the boundary
        minScore = (minScore>score) ? score : minScore; //resetting the boundary
    };
    cout << amazingTurns << endl;
}

int main(){
    solve();
    return 0;
}
