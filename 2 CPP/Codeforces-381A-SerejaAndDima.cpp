//we use a two pointer approach
//these 2 pointers get dynamincally updated as we traverse the vector
//

#include <bits/stdc++.h>
using namespace std;

void solve() {
    int cards;
    cin >> cards;
    vector <int> nums;
    int n;
    while(cin>>n){
        nums.push_back(n);
    }
    
    int sereja = 0, dima = 0;
    int l = 0, r = cards-1; // creating 2 dynamic pointers..
    for(int i=0;i<cards;++i){
        int maxNum;
        if(nums[l]>nums[r]){
            maxNum = nums[l];
            l+=1;
        }
        else{
            maxNum = nums[r];
            r-=1;
        };

        if(i%2==0){
            sereja += maxNum;
        }
        else{
            dima+=maxNum;
        };
    }
    
    cout << sereja <<" "<< dima << endl;
}

int main(){
    solve();
    return 0;
}
