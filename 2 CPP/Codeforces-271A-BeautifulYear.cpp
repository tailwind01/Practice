#include <bits/stdc++.h>
using namespace std;

void solve(){
    int y;
    cin >> y ;
    string ans;
    //lets calculate the answer at the input stage itself
    for(int i=y+1;i<10001;++i){
        string year = to_string(i);
        set <char> digits(year.begin(),year.end());
        if(digits.size()==4){
            ans = year;
            break; //we get the f out of the loop after finding our answer :D
        }
        
    }
    cout << ans << endl; 
};

int main(){
    ios_base::sync_with_stdio (false);
    solve();
    return 0;
}
