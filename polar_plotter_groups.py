import csv
import matplotlib.pyplot as plt
import numpy as np

def read_csv_groups(filename, angle_column=None, amplitude_column=None):
    groups = [[], []]
    current_group = 0
    
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)
        
        if angle_column is None or amplitude_column is None:
            angle_column = next((i for i, h in enumerate(headers) if 'angle' in h.lower()), None)
            amplitude_column = next((i for i, h in enumerate(headers) if 'amplitude' in h.lower()), None)
        
        if angle_column is None or amplitude_column is None:
            raise ValueError(f"Cannot find appropriate column names. Available columns: {headers}")
        
        for row in csvreader:
            if not row:  # Empty line, switch to next group
                current_group = 1
                continue
            
            if len(row) > max(angle_column, amplitude_column):
                phase_angle = float(row[angle_column])
                amplitude = float(row[amplitude_column])
                groups[current_group].append((phase_angle, amplitude))
    
    return [np.array(group) for group in groups]

def create_polar_scatter_plot(groups, rotation_angle):
    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))
    
    colors = ['red', 'blue']
    for i, group in enumerate(groups):
        if group.size > 0:
            phase_angles, amplitudes = group[:, 0], group[:, 1]
            rotated_angles = (phase_angles + rotation_angle) % 360
            # Convert angles to radians and shift by pi/2 to start at right side
            plot_angles = np.radians((360 - rotated_angles) % 360 + 90)
            ax.scatter(plot_angles, amplitudes, c=colors[i], marker='o', s=20, label=f'Group {i+1}')
    
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
    
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    
    plt.tight_layout()
    plt.show()

def main():
    filename = '/Users/phil/dev/scripts/Quadrature_Test_Data_groups.csv'  # Replace with your CSV file name
    
    # Prompt for rotation angle
    rotation_angle = float(input("Enter phase rotation angle in degrees: "))
    
    try:
        groups = read_csv_groups(filename)
        create_polar_scatter_plot(groups, rotation_angle)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please specify the correct column indices:")
        angle_column = int(input("Enter the index of the phase angle column (0-based): "))
        amplitude_column = int(input("Enter the index of the amplitude column (0-based): "))
        groups = read_csv_groups(filename, angle_column, amplitude_column)
        create_polar_scatter_plot(groups, rotation_angle)

if __name__ == "__main__":
    main()