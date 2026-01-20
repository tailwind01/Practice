#include <iostream>
using namespace std;

int main() {
    
    int nc;
    cin >> nc;
    
    for(int i=0; i<nc;i++){
        int a,b,c;
        cin >> a >> b >> c;
        int p1 = abs(a-1);
        int p2 = abs(b-c)+abs(c-1);
        int ans = 3; //by default we set the invariance amongst the lifts
        if (p1<p2){ans = 1;}
        else if(p2<p1){ ans = 2;};
        
        cout << ans << endl;
        
    };
    
    return 0;
}
