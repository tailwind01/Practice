package main
import "fmt"

func main(){
    var nc int
    fmt.Scan(&nc)
    for i:=0; i<nc; i++ {
        var a,b int
        fmt.Scan(&a, &b)
        var result int = a^b
        fmt.Println(result)
    }
}
