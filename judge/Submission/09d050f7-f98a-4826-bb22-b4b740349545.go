package main

import (
	"fmt"
    "bufio"
    "os"
    "bytes"
)

func main() {
	var N int
	var Sequence string
	var Pattern int = 9
    
    io_in := bufio.NewReader(os.Stdin)
    fmt.Fscan(io_in, &N)
    io_out := bytes.NewBufferString("")
	
	for i := 0; i < N; i++ {
		//Print space
		for j := 0; j + i < N - 1; j++ {
            fmt.Fprint(io_out, " ")
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
        fmt.Fprintln(io_out, Sequence)
	}
    fmt.Print(io_out.String())
}