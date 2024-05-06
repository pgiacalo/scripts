package main

import (
    "fmt"
    "math"
    "strconv"
    "bufio"
    "os"
    "strings"
)

// convertDBmToWatts converts dBm to Watts.
func convertDBmToWatts(dBm float64) float64 {
    return math.Pow(10, dBm/10) / 1000
}

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter the power in dBm: ")
    input, _ := reader.ReadString('\n')

    dBm, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
    if err != nil {
        fmt.Printf("Invalid input: %s\n", err)
        os.Exit(1)
    }

    watts := convertDBmToWatts(dBm)
    fmt.Printf("%f dBm is equivalent to %f Watts\n", dBm, watts)
}
