// two versions of the code, one version stores all the magnets (O(N)) and the other stores only 2 at a given 03:26
//
// v2
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int nc;
    cin >> nc;
    int currMagnet;
    cin >> currMagnet; // first magnet taken as input
    int ans = 1; //as the first magnet is already read in (which will be dynamically updated)
    for(int i=1;i<nc;++i){
        int Magnet;
        cin >> Magnet;
        ans += (currMagnet!=Magnet);
        currMagnet = (currMagnet!=Magnet) ? Magnet: currMagnet; //using ternary to change
    };
    
    cout << ans << endl;
};

int main(){
    solve();
    return 0;
};

//v1
//
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int nc;
    cin >> nc;
    vector <int> positions; //initialized this array with trivial zero as a placeholder
    
    for(int i=0;i<nc;++i){
        int Mag;
        cin >> Mag;
        positions.push_back(Mag);
    }
    
    int ans=1; //initialized as first magnet will not be in the loop//
    
    for (int j=1;j<positions.size();j++){
        ans+=(positions[j]!=positions[j-1]);
    };
    
    cout << ans << endl;
};

int main()
{
    solve();
    return 0;
}
