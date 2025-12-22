#/ tailwind
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#define ull unsigned long long
using namespace std;


int main() {
    
    int nq;
    cin >> nq;
    set <ull> mynums;
    set<int>::iterator it;
    
    for(int i=0; i<nq;++i){
        int o;
        ull x;
        cin >> o >> x;
        if(o==1){
            mynums.insert(x);
        }
        else if(o==2){
            mynums.erase(x);
        }
        else{
            if(mynums.count(x)!=0){
                cout << "Yes" << endl;
            }
            else{
                cout << "No" << endl;
            }
        }
    }
}
