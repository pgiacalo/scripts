import csv
import matplotlib.pyplot as plt
import numpy as np

def read_csv(filename, angle_column=None, amplitude_column=None):
    phase_angles = []
    amplitudes = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        headers = csvreader.fieldnames
        
        if angle_column is None:
            angle_column = next((h for h in headers if 'angle' in h.lower()), None)
        if amplitude_column is None:
            amplitude_column = next((h for h in headers if 'amplitude' in h.lower()), None)
        
        if angle_column is None or amplitude_column is None:
            raise ValueError(f"Cannot find appropriate column names. Available columns: {headers}")
        
        for row in csvreader:
            phase_angles.append(float(row[angle_column]))
            amplitudes.append(float(row[amplitude_column]))
    return np.array(phase_angles), np.array(amplitudes)

def create_polar_scatter_plot(phase_angles, amplitudes, rotation_angle):
    # Apply rotation
    rotated_angles = (phase_angles + rotation_angle) % 360
    
    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))
    
    # Convert angles to radians and shift by pi/2 to start at right side
    plot_angles = np.radians((360 - rotated_angles) % 360 + 90)
    ax.scatter(plot_angles, amplitudes, marker='o', s=20)
    
    # Set up the grid
    ax.set_theta_zero_location('E')  # Set 0 degrees to the right
    ax.set_theta_direction(-1)  # Set counter-clockwise direction
    
    # Create custom angle labels with reversed signs and 180 instead of -180
    angles = np.arange(0, 360, 22.5)
    labels = []
    for angle in angles:
        if angle == 0:
            labels.append('0°')
        elif angle == 180:
            labels.append('180°')
        elif angle < 180:
            labels.append(f'-{angle}°')
        else:
            labels.append(f'{360 - angle}°')
    
    ax.set_thetagrids(angles, labels)
    
    # Make circular and radial gridlines gray and dashed
    ax.grid(color='gray', linestyle='--', alpha=0.7)
    
    # Remove radial axis labels but keep the circular grid lines
    ax.set_yticklabels([])
    
    ax.set_title(f'Polar Scatter Plot (Rotated {rotation_angle}°)')
    
    # Remove "Amplitude" and "Phase Angle" labels
    ax.set_xlabel('')
    ax.set_ylabel('')
    
    plt.tight_layout()
    plt.show()

def main():
    filename = '/Users/phil/dev/scripts/Quadrature_Test_Data_groups.csv'  # Replace with your CSV file name
    
    # Prompt for rotation angle
    rotation_angle = float(input("Enter phase rotation angle in degrees: "))
    
    try:
        phase_angles, amplitudes = read_csv(filename)
        create_polar_scatter_plot(phase_angles, amplitudes, rotation_angle)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please specify the correct column names:")
        angle_column = input("Enter the name of the phase angle column: ")
        amplitude_column = input("Enter the name of the amplitude column: ")
        phase_angles, amplitudes = read_csv(filename, angle_column, amplitude_column)
        create_polar_scatter_plot(phase_angles, amplitudes, rotation_angle)

if __name__ == "__main__":
    main()