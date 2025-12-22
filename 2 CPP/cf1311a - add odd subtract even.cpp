//publisher tailwind, runtime 92ms, memory 0Kb, codeforces 800
#include <iostream>
using namespace std;

int sol(int a, int b){
    
    int diff, ct;
    
    if(a>b){
            diff = a-b;
            if(diff%2==0){
                ct = 1;
            }
            else{
                ct = 2;
            }
        }
    else if(b>a){
            diff = a-b;
            if(diff%2!=0){
                ct = 1;
            }
            else{
                ct = 2;
            }
        }
    else{
            ct = 0;
        }
    return ct;
}

int main() {
    int nc;
    cin >> nc;
    for(int i=0; i<nc;i++){
        int a,b;
        cin >> a >> b;
        cout << sol(a,b) << endl;
    }
    
    return 0;
}
