package main

import (
	"fmt"
)

func main() {
	var N int
	var Sequence string
	var Pattern int = 9
	
	fmt.Scanln(&N)
	
	for i := 0; i < N; i++ {
		//Print space
		for j := 0; j + i < N - 1; j++ {
			fmt.Print(" ")
		}
		
		//Print Sequence
		Sequence = ""
		for j := 0; j <= i; j++ {
			Sequence = fmt.Sprintf("%d%s", Pattern, Sequence)
			if Pattern == 0 {
				Pattern = 9
			} else {
				Pattern--
			}
		}
		fmt.Println(Sequence)
	}
}