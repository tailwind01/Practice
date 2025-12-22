//publisher tailwind, runtime 62ms, memory 0Kb
#include <iostream>
using namespace std;
int main() {
    
    int n;
    cin >> n;
    int xsum = 0;
    int ysum = 0;
    int zsum =0;
    for(int i=0;i<n;++i){
        int x,y,z;
        cin >> x >> y >> z;
        xsum = xsum+x;
        ysum = ysum+y;
        zsum = zsum+z;
    }
    if(xsum== 0 && ysum==0 && zsum==0){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
    
}
