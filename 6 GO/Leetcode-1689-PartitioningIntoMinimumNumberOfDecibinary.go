import "strings"

func minPartitions(n string) int {
    var s string = "987654321"
    ans := 0
    for i:=0;i<len(s);i++ {
        if strings.Contains(n,string(s[i])) {
            ans = int(s[i]-'0')
            break
        }
    }
    return ans
}
