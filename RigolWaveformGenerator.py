import math
import numpy as np

def generate_waveform(waveform_type, frequency, num_cycles):
    points_per_cycle = 8192 // num_cycles
    t = np.linspace(0, 1, points_per_cycle, endpoint=False)

    if waveform_type == "sine":
        waveform = 0.312 * np.sin(2 * np.pi * t)
    elif waveform_type == "square":
        waveform = 0.312 * np.sign(np.sin(2 * np.pi * t))
    elif waveform_type == "triangle":
        waveform = 0.624 * (np.abs(2 * (t - np.floor(t + 0.5))) - 0.5)
    elif waveform_type == "sawtooth":
        waveform = 0.624 * (t - 0.5)
    elif waveform_type == "raised_cosine":
        beta = 0.35  # Roll-off factor
        waveform = 0.312 * np.sinc(t) * np.cos(np.pi * beta * t) / (1 - (2 * beta * t)**2)
    elif waveform_type == "root_raised_cosine":
        beta = 0.35  # Roll-off factor
        waveform = 0.312 * np.sqrt(2) * ((1 - beta + 4 * beta / np.pi) * np.sinc((1 - beta) * t) +
                                         (1 + beta - 4 * beta / np.pi) * np.sinc((1 + beta) * t) -
                                         (4 * beta / np.pi) * np.cos((1 + beta) * np.pi * t))
    else:
        raise ValueError("Unsupported waveform type")

    # Repeat the waveform for the requested number of cycles
    full_waveform = np.tile(waveform, num_cycles)

    # Ensure we have exactly 8192 points
    if len(full_waveform) > 8192:
        full_waveform = full_waveform[:8192]
    elif len(full_waveform) < 8192:
        full_waveform = np.pad(full_waveform, (0, 8192 - len(full_waveform)), 'wrap')

    return full_waveform.tolist()

def write_csv(filename, waveform_type, frequency, num_cycles, waveform):
    with open(filename, 'w') as f:
        # Write header
        f.write("RIGOL:DG1:CSV DATA FILE\n")
        f.write("TYPE:Arb\n")
        f.write("AMP:0.647 Vpp\n")
        f.write(f"PERIOD:{1/frequency:.2E} S\n")
        f.write("DOTS:8192\n")
        f.write("MODE:Freq\n")
        f.write(f"AFG Frequency:{frequency:.1E}\n")
        f.write("AWG N:0\n")
        f.write("x,y[V]\n")

        # Write waveform data
        for value in waveform:
            f.write(f",{value:.4f}\n")

        # Write two empty lines at the end
        f.write("\n")

def main():
    waveform_types = ["sine", "square", "triangle", "sawtooth", "raised_cosine", "root_raised_cosine"]
    
    print("Select a waveform type:")
    for i, wt in enumerate(waveform_types, 1):
        print(f"{i}. {wt.replace('_', ' ').title()}")
    
    while True:
        try:
            waveform_choice = int(input("Enter the number of your choice: ")) - 1
            if 0 <= waveform_choice < len(waveform_types):
                waveform_type = waveform_types[waveform_choice]
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    frequency = float(input("Enter the frequency in MHz: ")) * 1e6  # Convert MHz to Hz
    num_cycles = int(input("Enter the number of complete waveform cycles: "))

    waveform = generate_waveform(waveform_type, frequency, num_cycles)
    
    filename = f"{waveform_type}_{int(frequency/1e6)}MHz_{num_cycles}_cycles.csv"
    write_csv(filename, waveform_type, frequency, num_cycles, waveform)
    
    print(f"CSV file '{filename}' has been generated.")

if __name__ == "__main__":
    main()