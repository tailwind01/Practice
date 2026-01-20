#include <iostream>
using namespace std;

int main() {
    
    int nc;
    cin >> nc;
    
    for(int i=0; i<nc;i++){
        int n,k;
        cin >> n >> k ;
        int stock = 0, ans = 0;
        
        for(int j=0; j<n; j++){
            int gold;
            cin >> gold;
            if(gold==0 and stock>0){
                stock-=1;
                ans +=1 ;
            };
            
            if (gold>=k){
                stock+=gold;
            };
        };
        
        cout << ans << endl;
    };
    
    return 0;
}
