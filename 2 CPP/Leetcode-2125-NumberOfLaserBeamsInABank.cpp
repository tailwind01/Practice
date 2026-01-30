class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int connections = 0, prevDocket = 0;
        for(int i=0;i<bank.size();++i){
            int ctOf1s = count(bank[i].begin(),bank[i].end(),'1');
            if(ctOf1s){
                connections+=(prevDocket*ctOf1s);
                prevDocket=ctOf1s;
            }

        }
        return connections;
    }
};
