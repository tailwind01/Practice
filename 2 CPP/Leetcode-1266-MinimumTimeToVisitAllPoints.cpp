class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int ans = 0;
        for(int i=0;i<points.size()-1;++i){
            vector <int> pt = points[i];
            vector <int> npt = points[i+1];
            int xdiff = abs(npt[0]-pt[0]);
            int ydiff = abs(npt[1]-pt[1]);
            ans+=max(xdiff,ydiff);
        }
        return ans;
    }
};
