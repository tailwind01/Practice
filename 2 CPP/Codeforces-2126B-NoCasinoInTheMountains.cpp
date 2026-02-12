#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,k;
    cin >> n >> k;
    vector <int> days(n);
    copy_n(istream_iterator <int> (cin), n, days.begin());
    int hikes = 0, zeroCt = 0;
    for(int i=0;i<n;i++){
        int num = days[i];
        if (num==0){
            zeroCt+=1;
            if(zeroCt==k){
                hikes+=1;
                zeroCt=-1; //set to -1 for the rest day after a hike
            }
        }
        else{
            zeroCt=0;
        }
    }

    cout << hikes << "\n";
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
