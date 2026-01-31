//0ms Solution
//
//
class Solution {
public:
    int minBitFlips(int start, int goal) {
        string s32 = bitset<32>(start).to_string();
        string g32 = bitset<32>(goal).to_string();
        int moves = 0;
        for(int i=0;i<g32.size();++i){
            moves+= (g32[i]!=s32[i]); //boolean addition
        }
        return moves;
    }
};
