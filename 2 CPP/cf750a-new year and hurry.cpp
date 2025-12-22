//publisher tailwind, runtime 46ms, memory 0Kb
#include <iostream>
using namespace std;
int main() {
    int n,m;
    cin >> n >> m;
    
    int time_to_solve = 4*60 - m;
    int solved = 0;
    while(time_to_solve>0 && n>0){
        int reqdT = 5*(solved+1);
        if(reqdT <= time_to_solve){
            time_to_solve-=reqdT;
            solved+=1;
            n-=1;
        }
        else{
            break;
        }
    }
    cout << solved << endl;
    return 0;
}
