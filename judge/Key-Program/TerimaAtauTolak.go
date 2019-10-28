package main

import "fmt"

func Solve(s string) bool {
	var curr byte = 'A';
	for _, bit := range s {
		if bit == '0' {
			switch curr {
				case 'A' :
					curr = 'B'
				case 'B' :
					curr = 'F'
				case 'C' :
					curr = 'E'
				case 'D' :
					curr = 'E'
				case 'E' :
					curr = 'I'
				case 'F' :
					curr = 'I'
				case 'G' :
					curr = 'D'
				case 'H' :
					curr = 'H'
				case 'I' :
					curr = 'H'
			}
		} else {
			switch curr {
				case 'A' :
					curr = 'E'
				case 'B' :
					curr = 'E'
				case 'C' :
					curr = 'H'
				case 'D' :
					curr = 'A'
				case 'E' :
					curr = 'H'
				case 'F' :
					curr = 'C'
				case 'G' :
					curr = 'G'
				case 'H' :
					curr = 'G'
				case 'I' :
					curr = 'H'
			}
		}
	}
	
	return curr == 'D' || curr == 'E'
}

func main() {
	var n int
	
	fmt.Scanln(&n)
	
	s := make([]string, n)
	
	for i := 0; i < n; i++ {
		fmt.Scanln(&s[i])
		if Solve(s[i]) {
			fmt.Printf("Case %d : Terima\n", i + 1)
		} else {
			fmt.Printf("Case %d : Tolak\n", i + 1)
		}
	}
}