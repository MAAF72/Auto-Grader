package main

import (
    "fmt"
    "bufio"
    "os"
    "bytes"
)

func main() {
    var (
        N int
    )
    
    io_in := bufio.NewReader(os.Stdin)
    fmt.Fscan(io_in, &N)
    io_out := bytes.NewBufferString("")
    for i := 1; i <= N; i++ {
        if i % 15 == 0 {
            fmt.Fprint(io_out, "HEYAHOOO ")
            //fmt.Print("HEYAHOOO ")
        } else if i % 5 == 0 {
            fmt.Fprint(io_out, "HOOO ")
            //fmt.Print("HOOO ")
        } else if i % 3 == 0 {
            fmt.Fprint(io_out, "HEYA ")
            //fmt.Print("HEYA ")
        } else {
            fmt.Fprint(io_out, i, " ")
            //fmt.Print(i, " ")
        }
    }
    fmt.Println(io_out.String())
    
}