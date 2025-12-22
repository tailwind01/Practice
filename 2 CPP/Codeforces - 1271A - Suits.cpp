//tailwind code, performs super fast, runtime 31 ms, memory 0 kb
#include <bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c,d,e,f;
    cin >> a >> b>> c>> d>> e>> f;
    int cost = 0;
    if(e>=f){
        vector <int> suit1 = {a,d};
        cost = cost +  *min_element(suit1.begin(), suit1.end())*e;
        d = d-*min_element(suit1.begin(), suit1.end());
        vector <int> suit2 = {b,c,d};
        cost = cost + *min_element(suit2.begin(), suit2.end())*f;
    }
    else{
        vector <int> suit2 = {b,c,d};
        cost = cost + *min_element(suit2.begin(), suit2.end())*f;
        d = d-*min_element(suit2.begin(), suit2.end());
        vector <int> suit1 = {a,d};
        cost = cost +  *min_element(suit1.begin(), suit1.end())*e;
    }
    
    cout << cost << endl;
}
