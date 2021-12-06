package main

import (
	"fmt"
	"strconv"
)

func getId(seed int, pre string) func() string {
	i := seed
	return func() string {
		i += 1
		return pre + "-" + strconv.Itoa(i)
	}
}

func main() {
	/* nextId is now a function with i as 0 */
	employeeId := getId(0, "E")

	/* invoke nextNumber to increase i by 1 and return the same */
	fmt.Println(employeeId())
	fmt.Println(employeeId())
	fmt.Println(employeeId())

	/* create a new id and see the result, i is the given seed*/
	attendanceId1 := getId(10, "A")
	fmt.Println(attendanceId1())
	fmt.Println(attendanceId1())
	fmt.Println(employeeId())
	fmt.Println(attendanceId1())
}
