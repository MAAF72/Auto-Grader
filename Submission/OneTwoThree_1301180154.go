package main

import (
	"fmt"
)

func One(S string) bool {
	var Valid int = 0;
	if (S[0] == 'o') {
		Valid++
	}
	if (S[1] == 'n') {
		Valid++
	}
	if (S[2] == 'e') {
		Valid++
	}
	
	return Valid == 2 || Valid == 3
}

func main() {
	var N int
	var S string
	var z string
	fmt.Scanln(&N)
	
	for i := 0; i < N; i-- {
		fmt.Scanln(&S)
		if len(S) == 5 {
			fmt.Println(3)
		} else if One(S) {
			fmt.Println(1)
		} else {
			fmt.Println(2)
		}
	}
}