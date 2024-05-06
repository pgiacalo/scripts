package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const speedOfLight = 299792458 // Speed of light in meters per second

func frequencyToWavelength(freqMHz float64) float64 {
	return speedOfLight / (freqMHz * 1e6)
}

func wavelengthToFrequency(wavelengthM float64) float64 {
	return speedOfLight / wavelengthM
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("------------------------------------")
	fmt.Println("Select conversion type:")
	fmt.Println("1: Frequency (MHz) to Wavelength (meters)")
	fmt.Println("2: Wavelength (meters) to Frequency (MHz)")
	fmt.Println("3: EXIT")

	for true {

		fmt.Println("------------------------------------")
		fmt.Print("Enter choice (1, 2 or 3): ")
		choiceInput, _ := reader.ReadString('\n')
		choiceInput = strings.TrimSpace(choiceInput)

		choice, err := strconv.Atoi(choiceInput)
		if choice == 3 {
			fmt.Println("Exiting...")
			os.Exit(1)
		}
		
		if err != nil || (choice != 1 && choice != 2) {
			fmt.Println("Invalid choice. Please enter 1, 2 or 3.")
			os.Exit(1)
		}

		if choice == 1 {
			fmt.Print("Enter frequency in MHz: ")
			input, _ := reader.ReadString('\n')
			freqMHz, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
			if err != nil {
				fmt.Println("Invalid input. Please enter a valid number.")
			}

			wavelength := frequencyToWavelength(freqMHz)
			fmt.Printf("Wavelength: %.1f meters\n", wavelength)
		} else {
			fmt.Print("Enter wavelength in meters: ")
			input, _ := reader.ReadString('\n')
			wavelengthM, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
			if err != nil {
				fmt.Println("Invalid input. Please enter a valid number.")
			}

			frequencyMHz := wavelengthToFrequency(wavelengthM) / 1e6
			fmt.Printf("Frequency: %.1f MHz\n", frequencyMHz)
		} 
	}

}
