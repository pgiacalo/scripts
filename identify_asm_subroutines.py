import re
import os

def count_subroutine_calls(file_path):
    subroutine_calls = {}
    
    # Regular expression pattern to match subroutine call lines
    call_pattern = re.compile(r'\bcall\s+0x([0-9a-fA-F]+)\b')

    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line contains a subroutine call
            match = call_pattern.search(line)
            if match:
                subroutine_address = match.group(1)
                # Add subroutine address to subroutine_calls dictionary
                if subroutine_address in subroutine_calls:
                    subroutine_calls[subroutine_address] += 1
                else:
                    subroutine_calls[subroutine_address] = 1
    
    # Sort subroutine_calls by the number of calls (descending)
    sorted_calls = sorted(subroutine_calls.items(), key=lambda x: x[1], reverse=True)
    
    # Print the results
    print("Subroutine Calls:")
    for address, count in sorted_calls:
        print(f"Subroutine at address 0x{address}: {count} calls")

# Example usage:
file_path = input("Enter the full path to the .asm file: ")
if os.path.exists(file_path) and file_path.endswith('.asm'):
    count_subroutine_calls(file_path)
else:
    print("Invalid file path or file type. Please provide the full path to an assembly language file (.asm)")
