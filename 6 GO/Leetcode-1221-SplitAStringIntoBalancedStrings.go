func balancedStringSplit(s string) int {
    var lseen,rseen,ans int = 0,0,0
    for i := 0; i < len(s); i++ {
        if s[i]=='L'{
            lseen++
        } else{
            rseen++
        }
        if lseen==rseen {ans++}
    }
    return ans;
}
