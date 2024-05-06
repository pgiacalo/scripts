#!/usr/bin/env python3
import os
import sys
import fnmatch
import re

BOLD = "\033[1m"
GREEN = "\033[32m"
RESET = "\033[0m"

total_files_processed = 0
total_dirs_processed = 0

def search_files(directory, pattern, max_depth=None, case_insensitive=False, search_directories=False):
    global total_files_processed, total_dirs_processed
    matched_paths = []

    if case_insensitive:
        pattern = pattern.lower()

    for root, dirs, files in os.walk(directory):
        if max_depth is not None:
            depth = root[len(directory):].count(os.path.sep)
            if depth > max_depth:
                del dirs[:]
                continue        

        if search_directories:
            for dirname in dirs:
                total_dirs_processed += 1
                target = dirname.lower() if case_insensitive else dirname
                if fnmatch.fnmatch(target, f"*{pattern}*"):
                    full_path = os.path.join(root, dirname)
                    matched_paths.append(full_path)
                print(f"\rProcessed {total_files_processed} files and {total_dirs_processed} directories...", end='')

        for filename in files:
            total_files_processed += 1
            target = filename.lower() if case_insensitive else filename
            if fnmatch.fnmatch(target, f"*{pattern}*"):
                full_path = os.path.join(root, filename)
                matched_paths.append(full_path)
            if search_directories:
                print(f"\rProcessed {total_files_processed} files and {total_dirs_processed} directories...", end='')
            else:
                print(f"\rProcessed {total_files_processed} files (directory names excluded)...", end='')

    return matched_paths

def print_usage():
    print("Searches file and/or directory names starting in the given directory looking for a pattern within the name.")
    print("Usage: fsearch DIRECTORY \"PATTERN\" [MAX_DEPTH] [OPTIONS]")
    print("\nOptions:")
    print("  -i       : Perform a case-insensitive search.")
    print("  -d       : Search directory names in addition to file names.")
    print("  -h/--help: Display this help message.")

if __name__ == "__main__":
    if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:
        print_usage()
        sys.exit(0)

    dir_to_search = sys.argv[1]
    pattern = sys.argv[2]
    depth = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else None
    case_insensitive = "-i" in sys.argv
    search_directories = "-d" in sys.argv

    matches = search_files(dir_to_search, pattern, depth, case_insensitive, search_directories)
    print("\n")  # To move to the next line after processing counter completes

    if matches:
        print(f"{len(matches)} matches found after searching {total_files_processed} files and {total_dirs_processed} directories:")
        for match in matches:
            highlighted_match = re.sub(pattern, lambda m: BOLD + GREEN + m.group() + RESET, match, flags=re.IGNORECASE if case_insensitive else 0)
            print(highlighted_match)
    else:
        if search_directories:
            print(f"No matches found after searching {total_files_processed} files and {total_dirs_processed} directories.")
        else:
            print(f"No matches found after searching {total_files_processed} files (directory names excluded).")
