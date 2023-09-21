#!/usr/bin/env python3
import os
import sys
import fnmatch
import shutil
import re

BOLD = "\033[1m"
GREEN = "\033[32m"
RESET = "\033[0m"

def backup_file(filename):
    backup_filename = filename + '.bak'
    shutil.copy2(filename, backup_filename)
    return backup_filename

def search_and_replace(filename, search_string, replacement_string=None, case_sensitive=True):
    global files_remaining

    changes_made = False
    output_lines = []

    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        for line_no, line in enumerate(file, 1):
            compare_line = line.lower() if not case_sensitive else line
            compare_string = search_string.lower() if not case_sensitive else search_string

            if compare_string in compare_line:
                highlighted_line = re.sub(search_string, lambda match: BOLD + GREEN + match.group() + RESET, line, flags=re.IGNORECASE if not case_sensitive else 0)
                matched_files.append((filename, line_no, highlighted_line))
                
                if replacement_string:
                    line = re.sub(search_string, replacement_string, line, flags=re.IGNORECASE if not case_sensitive else 0)
                    changes_made = True

            output_lines.append(line)

    if changes_made:
        backup_file(filename)
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(output_lines)
        print(f"\rReplacements made in {filename}")

    files_remaining -= 1
    print(f"\r{files_remaining} files remaining...", end='')

def count_files(directory, file_types, max_depth=None):
    file_patterns = ['*.' + ft.lstrip('.') for ft in file_types]
    count = 0

    for root, dirs, files in os.walk(directory):
        if max_depth is not None:
            depth = root[len(directory) + len(os.path.sep):].count(os.path.sep)
            if depth > max_depth:
                del dirs[:]
                continue

        for file_pattern in file_patterns:
            for filename in fnmatch.filter(files, file_pattern):
                count += 1

    return count

def search_directory(directory, search_string, file_types, max_depth=None, callback=None, case_sensitive=True):
    file_patterns = ['*.' + ft.lstrip('.') for ft in file_types]

    for root, dirs, files in os.walk(directory):
        if max_depth is not None:
            depth = root[len(directory) + len(os.path.sep):].count(os.path.sep)
            if depth > max_depth:
                del dirs[:]
                continue

        for file_pattern in file_patterns:
            for filename in fnmatch.filter(files, file_pattern):
                if callback:
                    callback(os.path.join(root, filename), search_string, replacement_str, case_sensitive)

if __name__ == "__main__":
    if len(sys.argv) < 2 or '-h' in sys.argv:
        print("Searches file contents from the current directory looking for a given string.")
        print("Usage: search \"SEARCH_STRING\" \"FILE_TYPES\" [MAX_DEPTH] [-i] [-r \"REPLACEMENT_STRING\"]")
        print("\nOptions:")
        print("-i\t\tCase insensitive search")
        print("-r\t\tReplace mode. Requires a replacement string")
        sys.exit(1)

    search_str = sys.argv[1]
    types = [t.lstrip('.') for t in sys.argv[2].split(',')]
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

    total_files = count_files(os.getcwd(), types, depth)
    print(f"Searching through {total_files} files...")

    files_remaining = total_files
    matched_files = []

    search_directory(os.getcwd(), search_str, types, depth, search_and_replace, case_sensitive)

    print("\n")  # move to the next line after countdown completes

    for filename, line_no, line in matched_files:
        print(f"Found in {filename} on line {line_no}: {line.strip()}")
