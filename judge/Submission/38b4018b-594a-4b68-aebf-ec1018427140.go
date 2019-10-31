package main

import "fmt"
import "sort"

func create2DMatrix(x int, y int) [][]int {
	matrix2d := make([][]int, x)
	
	for i := range matrix2d {
		matrix2d[i] = make([]int, y)
	}
	return matrix2d
}

func BFS(n int, ini int, matrix [][]int) []int {
	var queue []int
	var result []int
	var curr int
	
	visited := make([]bool, n)//auto false, default/zero value of boolean
	queue = append(queue, ini)
	
	visited[ini] = true
	
	for len(queue) > 0 {
		curr, queue = queue[0], queue[1:]
		
		for _, adj := range matrix[curr] {
			if visited[adj] == false {
				queue = append(queue, adj)
				visited[adj] = true
			}
		}
	}
	
	
	for i := 0; i < n; i++ {
		if visited[i] == false {
			result = append(result, i)
		}
	}
	
	return result
}

func main() {
	var (
		n, m, alpha int
		src, dest, ini byte
	)
	
	fmt.Scanln(&n, &m)
	
	matrix := create2DMatrix(n, 0)
	
	for i := 0; i < m; i++ {
		fmt.Scanf("%c %c %d\n", &src, &dest, &alpha)

		matrix[int(src) - int('A')] = append(matrix[int(src) - int('A')], int(dest) - int('A'))
		
	}
	fmt.Scanf("%c\n", &ini)
	
	result := BFS(n, int(ini) - int('A'), matrix)
	sort.Ints(result)
	
	fmt.Print("{")
	
	if len(result) > 0 {
		for i := 0; i < len(result) - 1; i++ {
			fmt.Printf("%c, ", byte(int(result[i]) + int('A')))
		}
		fmt.Printf("%c", byte(int(result[len(result) - 1]) + int('A')))
	}
	
	fmt.Print("}\n")
}