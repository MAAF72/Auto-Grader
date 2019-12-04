package main

import (
	"fmt"
	"math"
)


func Pythagoras(A, B float64) float64 {
	return math.Sqrt(A*A + B*B)
}

func main() {
	var R, W, L float64
	fmt.Scan(&R)
	
	i := 1
	for R != 0 {
		fmt.Scanln(&W, &L)
		
		fmt.Print("Case ", i, " : ")
		
		if 2*R >= Pythagoras(W, L) {
			fmt.Println("Muat")
		} else {
			fmt.Println("Tidak")
		}
		
		fmt.Scan(&R)
		i++
	}
}

