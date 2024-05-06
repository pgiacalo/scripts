#!/usr/bin/env python3
import os
import sys
import fnmatch
import shutil

BOLD = "\033[1m"
GREEN = "\033[32m"
RESET = "\033[0m"

def backup_file(filename):
    backup_filename = filename + '.bak'
    shutil.copy2(filename, backup_filename)
    return backup_filename

def find_and_replace_in_file(filename, search_string, replacement_string=None, case_sensitive=True):
    changes_made = False
    output_lines = []

    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        for line_no, line in enumerate(file, 1):
            compare_line = line.lower() if not case_sensitive else line
            compare_string = search_string.lower() if not case_sensitive else search_string

            if compare_string in compare_line:
                highlighted_line = line.replace(search_string, BOLD + GREEN + search_string + RESET)
                print(f"Found in {filename} on line {line_no}: {highlighted_line.strip()}")

                if replacement_string:
                    if not changes_made:
                        backup_file(filename)  # Backup the original file before making any changes
                        changes_made = True

                    line = line.replace(search_string, replacement_string)

            output_lines.append(line)

    if changes_made:
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(output_lines)
        print(f"Replacements made in {filename}")


def search_directory(directory, search_string, file_types, max_depth=None, replacement_string=None, case_sensitive=True):
    file_patterns = ['*.' + ft for ft in file_types]

    for root, dirs, files in os.walk(directory):
        if max_depth is not None:
            depth = root[len(directory) + len(os.path.sep):].count(os.path.sep)
            if depth > max_depth:
                del dirs[:]
                continue

        for file_pattern in file_patterns:
            for filename in fnmatch.filter(files, file_pattern):
                find_and_replace_in_file(os.path.join(root, filename), search_string, replacement_string, case_sensitive)

if __name__ == "__main__":
    if len(sys.argv) < 3 or '-h' in sys.argv:
        print("Usage: ./search.py \"SEARCH_STRING\" \"FILE_TYPES\" [MAX_DEPTH] [-i] [-r \"REPLACEMENT_STRING\"]")
        sys.exit(1)

    search_str = sys.argv[1]
    types = sys.argv[2].split(',')
    depth = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else None
    case_sensitive = False if '-i' in sys.argv else True

    replace_mode = '-r' in sys.argv
    replacement_str = None
    if replace_mode:
        try:
            idx = sys.argv.index('-r')
            replacement_str = sys.argv[idx + 1]
        except (ValueError, IndexError):
            print("Error: Please specify the replacement string after the '-r' flag.")
            sys.exit(1)

    print("Searching...")
    search_directory(os.getcwd(), search_str, types, depth, replacement_str, case_sensitive)
