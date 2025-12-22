//signed tailwind, 0.25 sec execution, less than 2Mbs memory

#include <iostream>
#include <vector>
using namespace std;
int main()
{
   int numcases;
   cin >> numcases;
   int maxnum = 100001; vector <unsigned long long int> allnums={0,1,1};
    
    for(int i=3; i<maxnum;i++){
        if(i%2==0){
            unsigned long long int mplier = i/2;
            allnums.push_back(mplier*i - 1);
        }
        else{
            unsigned long long int mplier = i/2;
            unsigned long long int addn = i/2 -1 ;
            allnums.push_back(mplier*i + addn);
        }
    }
   
   for(int j=0; j<numcases;j++){
       int givennum;
       cin >> givennum;
       cout << allnums[givennum] << endl;
   }
   return 0;
}
