#include <iostream>
#include <list>
#include <set>
using namespace std;

int main(){
    int nc;
    cin >> nc;
    
    for(int i=0;i<nc;i++){
        list <int> sizes;
        for (int j = 0;j<4;j++){
            int Num;
            cin >> Num;
            sizes.push_back(Num);
        };
        
        set <int> vertices(sizes.begin(),sizes.end());
        
        if(vertices.size()==1){
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }
    return 0;
}
