#include <iostream>
#include <string>
#include <vector>
using namespace std;

void solve(){
    int n, k;
    cin >> n >> k ;
    // int ans = 0;
    
    vector<int> scores;
    
    for (int i=0; i<n; ++i){
        int score;
        cin >> score;
        scores.push_back(score);
    };
    
    int ans = 0;
    for (int j=0; j<n;j++){
        if (scores[j]>=scores[k-1] and scores[j]>0){
            ans+=1;
        };
    };
    
    cout << ans << endl;
}


int main(){
    solve();
}
