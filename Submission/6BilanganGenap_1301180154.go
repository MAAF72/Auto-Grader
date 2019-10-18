package main

import (
	"fmt"
)

func main() {
	var N, i int
	
	fmt.Scanln(&N)
	
	if N % 2 == 0 {
		N++
	}
	
	i = 0
	
	for i < 6 {
		fmt.Println(N)
		N += 2
		i++
	}
}