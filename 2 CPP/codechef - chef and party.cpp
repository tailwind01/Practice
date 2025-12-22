// a tailwind publication
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int nc;
    cin >> nc;
    for(int i=0; i<nc;i++){
        int nums;
        cin >> nums;
        vector <int> arr;
        for(int j=0; j<nums;j++){
            int req;
            cin >> req;
            arr.push_back(req);
        }
        sort(arr.begin(),arr.end());
        if(arr[0]==0){
            int frCt=0;
            for(int m=0; m<nums;m++){
                if(frCt>=arr[m]){
                    frCt = frCt+1;
                }
            }
            cout << frCt << endl;
        }
        else{
            cout << 0 << endl;
        }
    }

    return 0;
}
