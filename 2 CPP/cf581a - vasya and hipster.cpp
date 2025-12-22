//publisher tailwind, runtime 31ms, memory 0Kb
#include <iostream>
using namespace std;
int main() {
    int r, b, ans1, ans2;
    cin >> r >> b;
    
    if(r>=b){
        ans1 = b;
        ans2 = (r-b)/2;
    }
    else{
        ans1 = r;
        ans2 = (b-r)/2;
    }
    
    cout << ans1 <<" " << ans2 <<endl;

    return 0;
}
