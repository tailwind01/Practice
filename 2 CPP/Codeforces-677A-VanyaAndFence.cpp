#include <bits/stdc++.h>
using namespace std;

void solve(){
    int f, h;
    cin >> f >> h;
    int width = 0;
    //lets calculate the answer at the input stage itself
    for(int i=0;i<f;++i){
        int pheight;
        cin >> pheight;
        int pw = 1;
        if(pheight>h){
            pw=2;
        };
        width+=pw;
    }
    cout << width << endl; 
};

int main(){
    solve();
    return 0;
}
