package main

import (
    "fmt"
)

func One(S string) bool {
    var Valid int = 0
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
    var Result int = 0
	var Word string
    fmt.Scanln(&N)
	for i := 0; i < N; i++ {
		fmt.Scan(&Word)
		
		if len(Word) == 5 {
			Result += 3
		} else if len(Word) == 4 {
			Result += 4
		} else if One(Word) {
			Result += 1
		} else {
			Result += 2
		}
	}
    fmt.Println(Result)
}
