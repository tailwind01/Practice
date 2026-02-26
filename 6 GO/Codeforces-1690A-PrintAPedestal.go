package main

import "fmt"

func solve(n int) (int, int, int) {
	var second, first, third int
	if n%3 == 0 {
		second = n / 3
	} else {
		second = (n + 3) / 3
	}
	first = second + 1
	third = n - first - second
	if third == 0 {
		third++
		second--
	}
	return second, first, third
}

func main() {
	var nc int
	fmt.Scan(&nc)
	for i := 0; i < nc; i++ {
		var num int
		fmt.Scan(&num)
		s, f, t := solve(num)
		fmt.Println(s, f, t)
	}
}
