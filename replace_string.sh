#!/bin/bash

# Navigate to the desired directory
# cd /path/to/directory

# Loop through all .txt files in the current directory
for file in *.txt; do
    # Check if the file exists
    if [[ -f "$file" ]]; then
        # Use sed to replace "kHz" with "kilohertz"
        sed -i '' 's/GHz/gigahertz/g' "$file"
    fi
done
