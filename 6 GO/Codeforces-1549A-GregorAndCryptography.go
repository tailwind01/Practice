package main
import "fmt"

func solve(P int) (int,int) {
  return 2,P-1
}

func main() {
	var nc int
	fmt.Scan(&nc)
	for i:=0; i<nc;i++{
	    var P int
	    fmt.Scan(&P)
	    a1,a2 := solve(P)
	    fmt.Println(a1,a2)
	}
}
