package main

import "fmt"

func create4DMatrix(w int, x int, y int, z int) [][][][]int {
	matrix4d := make([][][][]int, w)
	
	for i := range matrix4d {
		matrix4d[i] = make([][][]int, x)
		for j := range matrix4d[i] {
			matrix4d[i][j] = make([][]int, y)
			for k := range matrix4d[i][j] {
				matrix4d[i][j][k] = make ([]int, z)
			}
		}
	}
	return matrix4d
}

func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}

func main() {
	var (
		N, K, TotA, TotB, TotC, TotD int
	)
	
	fmt.Scanln(&N, &K)
	fmt.Scanln(&TotA, &TotB, &TotC, &TotD)
	
	ValP := make([]int, N)
	ValA := make([]int, N)
	ValB := make([]int, N)
	ValC := make([]int, N)
	ValD := make([]int, N)
	DP := create4DMatrix(TotA + 1, TotB + 1, TotC + 1, TotD + 1)
	
	for i := 0; i < N; i++ {
		fmt.Scanln(&ValA[i], &ValB[i], &ValC[i], &ValD[i], &ValP[i])
	}
	
	for e := 0; e < N; e++ {
		for m := 0; m < K; m++ {
			for i := TotA; i >= ValA[e]; i-- {
				for j := TotB; j >= ValB[e]; j-- {
					for k := TotC; k >= ValC[e]; k-- {
						for l := TotD; l >= ValD[e]; l-- {
							DP[i][j][k][l] = max(int(DP[i][j][k][l]), ValP[e] + DP[i - ValA[e]][j - ValB[e]][k - ValC[e]][l - ValD[e]])
						}
					}
				}
			}
		}
	}
	
	fmt.Println(DP[TotA][TotB][TotC][TotD])
}