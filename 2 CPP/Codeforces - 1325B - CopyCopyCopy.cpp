//tailwind pub
#include <iostream>
#include <set>
using namespace std;

int main(){
    int nc;
    cin>>nc;
    for(int i=0; i<nc;i++){
        int size;
        cin >> size;
        set <int> myset;
        for(int j=0;j<size;j++){
            int num;
            cin >> num;
            myset.insert(num);
        }
        cout << myset.size() << endl;
    }
}
