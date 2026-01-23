//heart of this problem is not the data collection, but the correction for overflow from overlapping
//so I have implemented the final if condition to account for that, which mathematically collapses
//several situations regarding the maximum height's leftmost index and minimum height's rightmost index

#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n ;
    
    vector <int> heights;
    
    for(int i=0;i<n;++i){
        int height;
        cin >> height;
        heights.push_back(height);
    };
    
    int maxH = *max_element(heights.begin(),heights.end());
    int minH = *min_element(heights.begin(),heights.end());
    auto itLeftMax = find(heights.begin(),heights.end(),maxH);
    int maxIndexLeft = distance(heights.begin(),itLeftMax); //leftmost maxima index
    auto itRightMin = find(heights.rbegin(),heights.rend(),minH); //rightmost minima index
    int minIndex = distance(heights.rbegin(),itRightMin);
    
    int ans = maxIndexLeft+minIndex;
    
    //in order to correct the overlapping situation where even a normal operation will double count
    //basically to deal with the overflow that happens by using the traversal
    //this condition is to correct for the passage of max and min with each other
    if(maxIndexLeft+minIndex >= n){
        ans-=1;
    }
    
    cout << ans << endl;
};

int main(){
    solve();
    return 0;
};
