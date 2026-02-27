package main
import "fmt"

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main(){
    var n int
    fmt.Scan(&n)
    var original string
    fmt.Scan(&original)
    var target string
    fmt.Scan(&target)
    var ans int = 0 
    for i:=0;i<n;i++ {
        var ato, att int
        ato = int((original[i])-'0')
        att = int((target[i])-'0')
        var diff int = abs(ato-att)
        ans += min(diff,10-diff)
    }
    fmt.Println(ans)
}
