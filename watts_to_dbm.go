package main

import (
    "bufio"
    "fmt"
    "math"
    "os"
    "strconv"
    "strings"
)

// convertWattsToDBm converts Watts to dBm.
func convertWattsToDBm(watts float64) float64 {
    return 10 * math.Log10(watts*1000)
}

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter the power in Watts: ")
    input, _ := reader.ReadString('\n')

    watts, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
    if err != nil {
        fmt.Printf("Invalid input: %s\n", err)
        os.Exit(1)
    }

    dBm := convertWattsToDBm(watts)
    fmt.Printf("%f Watts is equivalent to %f dBm\n", watts, dBm)
}
