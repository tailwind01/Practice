//using mathematical intuition
//

#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        // instead of storing numbers, we shall take just the counts for processing
        int p1 = 0, m1=0;
        for(int i=0;i<n;++i){
            int num;
            cin >> num;
            if (num==1){
                p1+=1;
            }
            else{
                m1+=1;
            }
        }
        
        int operations = 0;
        
        //for sum correction
        if(p1<m1){
            operations = ((m1-p1)%2!=0) ? (m1+1-p1)/2 : (m1-p1)/2;
        }
        operations += (m1-operations)%2; //for product correction
        
        cout << operations << "\n";
    }
}

int main(){
    solve();
    return 0;
}


//using list traversal..
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector <int> nums;
        for(int i=0;i<n;++i){
            int num;
            cin >> num;
            nums.push_back(num);
        }
        sort(nums.begin(),nums.end());
        int operations = 0;
        for(int j=0;j<n;++j){
            if(accumulate(nums.begin(),nums.end(),0)<0 or count(nums.begin(),nums.end(),-1)%2!=0){
                nums[j]=1;
                operations+=1;
            }
            else{
                break;
            }
        }
        cout << operations << "\n";
    }
}

int main(){
    solve();
    return 0;
}
