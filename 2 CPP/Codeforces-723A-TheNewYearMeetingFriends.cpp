#include <bits/stdc++.h>
using namespace std;

void solve() {
    int a,b,c;
    cin >> a >> b >> c;
    vector <int> distances = {a,b,c};
    sort(distances.begin(),distances.end());
    int ans = distances[2]-distances[0]; //as we made the midpoint the distance travelled to for each//
    cout << ans << endl;
}

int main(){
    solve();
    return 0;
}
