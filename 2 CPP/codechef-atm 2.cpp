// a tailwind publication
#include <iostream>
using namespace std;
int main() {
    
    int nc;
    cin >> nc;
    
    for(int i=0;i<nc;i++){
        int n,k,amtL;
        cin >> n >> k;
        amtL = k;
        for(int j=0; j<n;j++){
            int req;
            cin >> req;
            if(j<n-1){
                if(req<=amtL){
                    amtL = amtL - req;
                    cout << 1;
                    
                }
                
                else{
                    cout << 0;
                }
            }
            
            else{
                if(req<=amtL){
                    amtL = amtL - req;
                    cout << 1 << endl;
                }
                else{
                    cout << 0 << endl;
                }
            }
        }
    }

    return 0;
}
