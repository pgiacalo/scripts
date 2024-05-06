#!/usr/bin/env python3
import sys

#GOOD 
# Terminal color codes
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"

def max_line_length(filename):
    '''Return the length of the longest line in the given file'''
    max_length = 0
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            max_length = max(max_length, len(line.strip()))
    return max_length

def search_file(target_file, search_str):
    '''Search a file for a string, return the matching line if found, else return None'''
    with open(target_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if search_str in line:
                return line.strip()
    return None

def check_match(value1, value2):
    '''Check if two values match based on the given criteria'''
    if value2 == "y" and "y" in value1:
        return True
    if value2.isdigit():
        return value2 in value1
    if value2 == "n" and "is not set" in value1:
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script_name <file_to_search> <search_criteria_file>")
        sys.exit(1)

    file_to_search = sys.argv[1]
    search_criteria_file = sys.argv[2]

    # Extract matching lines from file 1 based on search criteria in file 2
    extracted_lines = []
    with open(search_criteria_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if '=' in line:
                search_str, _ = line.split('=', 1)
                search_str = search_str.strip()
                match = search_file(file_to_search, search_str)
                if match:
                    extracted_lines.append(match)

    # Column widths
    col1_width = max(len(line) for line in extracted_lines) + 2
    col2_width = max_line_length(search_criteria_file) + 2
    col3_width = 15  # Fixed width for the match result column

def extract_value(line):
    '''Extract the value after the "=" sign from a given line'''
    if '=' in line:
        _, value = line.split('=', 1)
        return value.strip()
    return None

with open(search_criteria_file, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        if '=' in line:
            search_str, output_value = line.split('=', 1)
            search_str = search_str.strip()
            output_value = output_value.strip()
            
            match = search_file(file_to_search, search_str)
            
            if match:
                is_match = check_match(match, output_value)
                match_status = f"{GREEN}matches{RESET}" if is_match else f"{RED}error{RESET}"
                
                match_value = extract_value(match)
                if not is_match:
                    match = match.replace(match_value, f"{RED}{match_value}{RESET}")
                
                print(f"{match:<{col1_width}} {search_str + '=' + GREEN + output_value + RESET:<{col2_width}} {match_status:<{col3_width}}")
